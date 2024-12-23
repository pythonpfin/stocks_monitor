import streamlit as st
import pandas as pd
import numpy as np 
import yfinance as yf 
import plotly.express as px
from datetime import datetime 



def build_sidebar():
    st.write('main')
    ticker_list = pd.read_csv('ticker.csv')
    tickers = st.multiselect(label="Selecione as Empresas da bolsa",options=ticker_list,placeholder="Ticker")
    start_date = st.date_input("De",format="DD/MM/YYYY",value=datetime(2022,1,1))
    end_date = st.date_input("Ate",format="DD/MM/YYYY",value="today")
    tickers = [t+".SA" for t in tickers]
    
    
    
    if tickers:
        prices = yf.download(tickers,start=start_date,end=end_date)['Close']
       
        
    if tickers:
        if  len(tickers) == 1:
            prices = prices.to_frame(name=''.join(tickers))  
            ##prices = pd.DataFrame({'Ticker':prices.index, 'return':prices.values})
               
        #baixar ibov
        prices['IBOV'] = yf.download("^BVSP", start=start_date,end=end_date)['Close']
        prices.columns = prices.columns.str.rstrip(".SA")
    
    return tickers, prices
    

def build_main(tickers,prices):
    st.markdown(
    """
    <style> 
      div[data-testid="stElementToolbar"] > img  {
      border-radius: 100px !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
    )
    
    #calcuplar pesos iguais para os tickers
    weights = np.ones(len(tickers))/len(tickers)
    
    #Adicinar coluna portifolio e multiplicar em matriz retirnando a coluna IBOV
    prices['Portifolio'] = prices.drop("IBOV",axis=1) @ weights
    #Normalizar os valores 
    norm_prices = 100 * prices/prices.iloc[0]
    #calcular o percentual de retornos
    returns = prices.pct_change()[1:]
    #calcular a volaticidade anualizada
    vols = returns.std() * np.sqrt(252)
    #calcular o percentual de retorno
    rets = (norm_prices.iloc[-1] - 100) /100
    
    #Criar o dataframe com as colunas do dataframe 
    
    if len(tickers) == 1:
       df = pd.DataFrame(prices.columns,columns=['Ticker'])
    else:
        df = pd.DataFrame(prices.columns)
    ##adicionar a url da imagem no dataframe
    df['image'] = [f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{t}.png' for t in df['Ticker']]
    
    #Adicioanar o coluna dos retorno no dataframe
    df = pd.merge(df, pd.DataFrame({'Ticker':rets.index, 'return':rets.values}), on = "Ticker", how = "inner") 
    
        #Adicioanar o coluna de volaticidade no dataframe
    df = pd.merge(df, pd.DataFrame({'Ticker':vols.index, 'vols':vols.values}), on = "Ticker", how = "inner") 
    
    st.dataframe(df,
                  column_config={
                      "Ticker":st.column_config.Column(width=90),
                      "image": st.column_config.ImageColumn(width=50)
                  },hide_index=True
                  )
    
    col1,col2 = st.columns(2,gap='large')
    with col1:
          st.subheader("Desempenho Relativo")
          st.line_chart(norm_prices, height=600)
    with col2:
        st.subheader("Risco-Retorno")
        fig = px.scatter(
            x=vols,
            y=rets,
            text=vols.index,
            color=rets/vols,
            color_continuous_scale=px.colors.sequential.Bluered_r
        )
        fig.update_traces(
            textfont_color='white', 
            marker=dict(size=45),
            textfont_size=10,                  
        )
        fig.layout.yaxis.title = 'Retorno Total'
        fig.layout.xaxis.title = 'Volatilidade (anualizada)'
        fig.layout.height = 600
        fig.layout.xaxis.tickformat = ".0%"
        fig.layout.yaxis.tickformat = ".0%"        
        fig.layout.coloraxis.colorbar.title = 'Sharpe'
        st.plotly_chart(fig, use_container_width=True)

    
    
    
    # for t in prices.columns:
    #     col1,col2,col3,col4,col5 = st.columns(5)
    #     col1.image(f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{t}.png', width=80 )
    #     col2.write(t)
    
st.set_page_config(layout='wide')

with st.sidebar:
   tickers,prices =  build_sidebar()
   
   
st.title('Python para investidores')
build_main(tickers,prices)
    
    
    

