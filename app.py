import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid


st.set_page_config(
    page_title="Monito Stocks",
    layout="wide"
)

st.title ('Meu portifolio de investimento')


def sidebar():
    
    st.image('img\img.png')
    list_tickers =  pd.read_csv('ticker.csv')
    tickers = st.multiselect(label='Selecione ticker',options=list_tickers,placeholder='Ticker')
    tickers = [tc+'.SA' for tc in tickers]
    
    start_date = st.date_input("De", format="DD/MM/YYYY", value=datetime(2020,1,2))
    end_date = st.date_input("Até", format="DD/MM/YYYY", value="today")

    if tickers:
        prices = yf.download(tickers,start=start_date,end=end_date)['Close']
        # prices = prices.dropna(axis=1)
        prices = prices.replace(to_replace='None', value=np.nan)
        
        prices.columns = prices.columns.str.rstrip('.SA')
        #baixar cotação indice bovespa
        prices['IBOV'] = yf.download("^BVSP",start=start_date,end=end_date)['Close']
        return tickers,prices
    return None,None



def main(tickers,prices):
    st.write('Main')
    #variavel de peso iguais 
    weigths = np.ones(len(tickers))/len(tickers)
    #multiplicar 
    #excluir ibov para ficar igual os matrizes
    prices['Portifolio'] = prices.drop("IBOV",axis=1) @ weigths
    norm_price  = 100 * prices / prices.iloc[0]

    returns  = prices.pct_change(fill_method=None)[1:]
    #vol anualizadas
    vols = returns.std()*np.sqrt(252)
    #retorno pegar o ultimo preco tirar 100 e dividir por 100 para ter em %
    rets = (norm_price.iloc[-1] - 100)/100
     
    mygrid = grid(5,5,5,5,5,vertical_align="top")
    #criar os cards
    for t in prices.columns:
        c = mygrid.container(border=True)
        c.subheader(t,divider='red')
        #definir 3 colunas
        cA,cB,cC = c.columns(3)
        if t == "Portifolio":
           cA.image("img/dolar.svg")
        elif t == "IBOV":
             cA.image("img/ibov.svg")
        else:
            cA.image(f'https://raw.githubusercontent.com/pythonpfin/icon-b3/main/icon/{t}.png', width=85)
        cB.metric(label="retorno",value=f"{rets[t]:.0%}")
        cC.metric(label="volatilidade",value=f"{vols[t]:.0%}")
        #style metric carts
        style_metric_cards(background_color='rgba(255,255,255,0)',border_radius_px = 35)
        
    c1,c2 = st.columns(2,gap="large")

    with c1:
        st.subheader('Desempenho relativo')
        st.line_chart(norm_price,height=600)

    with c2:
        st.subheader('Risco Retorno')
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



    st.dataframe(prices)


if __name__ == "__main__":

    with st.sidebar:
        tickers, prices = sidebar() 
    
    if tickers:
        main(tickers,prices)



    