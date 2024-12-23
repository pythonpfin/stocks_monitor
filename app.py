import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid

import os


st.set_page_config(
    page_title="Monitor Stocks",
    layout="wide"
)

st.title ('Meu portifolio de investimento')
st.divider()

st.html("styles.html")


# st.markdown("""
    # <style>
    # div[data-testid="metric-container"] {
    # background-color: rgba(28, 131, 225, 0.1);
    # border: 1px solid rgba(28, 131, 225, 0.1);
    # padding: 5% 5% 5% 10%;
    # border-radius: 5px;
    # color: rgb(30, 103, 119);
    # overflow-wrap: break-word;
    # }

    # /* breakline for metric text         */
    # div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
    # overflow-wrap: break-word;
    # white-space: break-spaces;
    # color: red;
    # }
    # </style>
    # """
    # , unsafe_allow_html=True)
    
    # st.markdown("""
    # <style>
    # div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
    # overflow-wrap: break-word;
    # white-space: break-spaces;
    # color: red;
    # }
    # div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div  {
    # font-size: 10% !important;
    # }
    # </style>
    # """
    # , unsafe_allow_html=True)
    
    
#     style_image1 = """
#     width: auto;
#     max-width: 850px;
#     height: auto;
#     max-height: 750px;
#     display: block;
#     justify-content: center;
#     border-radius: 20%;
#     """

#     style_image2 = """
#     width: auto;
#     max-width: 900px;
#     height: auto;
#     max-height: 800px;
#     display: block;
#     justify-content: center;
#     border-radius: 30%;
# """

# style_image3 = """
#     <style>
#     img {
#     max-width: 100%;
#     height: auto;
#     border-radius: 200px;
#     }
#     </style>
#      """
# st.markdown(style_image3, unsafe_allow_html=True)


#     st.markdown(
#         f'<img src="{"https://people.com/thmb/TzDJt_cDuFa_EShaPF1WzqC8cy0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(216x0:218x2)/michael-jordan-435-3-4fc019926b644905a27a3fc98180cc41.jpg"}" style="{style_image1}">',
#         unsafe_allow_html=True,
#     )

#     st.markdown(
#         f'<img src="{"https://people.com/thmb/TzDJt_cDuFa_EShaPF1WzqC8cy0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(216x0:218x2)/michael-jordan-435-3-4fc019926b644905a27a3fc98180cc41.jpg"}" style="{style_image2}">',
#         unsafe_allow_html=True,
#     )
    
#     st.markdown(
#         f'<img src="{"https://people.com/thmb/TzDJt_cDuFa_EShaPF1WzqC8cy0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(216x0:218x2)/michael-jordan-435-3-4fc019926b644905a27a3fc98180cc41.jpg"}" style="{style_image3}">',
#         unsafe_allow_html=True,
#     )
    
    
    
    # style_image3 = """
    # <style>
    #  div.css-1r6slb0.e1tzin5v2 {
    # background-color: #FFFFFF;
    # border: 1px solid #CCCCCC;
    # padding: 5% 5% 5% 10%;
    # border-radius: 5px;
    # border-left: 0.5rem solid #9AD8E1 !important;
    # box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;
    
    # }
    # </style>
    #  """
    # st.markdown(style_image3, unsafe_allow_html=True)
    
    # div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
    # overflow-wrap: break-word;
    # white-space: break-spaces;
    # color: red;
    # fonte-size: 10px !important
    # }
    # div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div p {
    # font-size: 10px !important
    # }
    
                            # st.markdown(
                            #     """
                            #     <style>
                                    
                            #     div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
                            #     overflow-wrap: break-word;
                            #     white-space: break-spaces;
                            #     color: red;
                            #     font-size: 100%;
                            #     }
                                    
                            #         div[data-testid="stMarkdownContainer"] > p {
                            #         font-size: 100% !important;
                                    
                            #         }
                                    
                            #         div[data-testid="stMetricValue"] > div  {
                            #         font-size: 45% !important;
                            #         padding: 10% 10% 10% 10%;
                            #         }
                            #         div[data-testid="stImage"] > img  {
                            #         border-radius: 50% !important;
                            #         }
                                    
                            #         </style>
                            #         """,
                            #     unsafe_allow_html=True,
                            #     )
                            
                            # custom_html = """
                            #     <div class="banner">
                            #     <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
                            #     </div>
                            #     <style>
                            #     .banner {
                            #     width: 160%;
                            #     height: 200px;
                            #     overflow: hidden;
                            #     }
                            #     .banner img {
                            #     width: 100%;
                            #     object-fit: cover;
                            #     }
                            #     </style>
                            #     """
                            #     # Display the custom HTML
                            # st.components.v1.html(custom_html)
                                
                            # st.markdown("""
                            #     <style>
                            #     .big-font {
                            #     font-size:200px !important;
                            #     }
                            #     </style>
                            #     """, unsafe_allow_html=True)


def sidebar():
    
    ##st.image('img/EMPRESA.png',width=100,caption='Minha empresa')
    st.logo('img/Logo2.png',link="https://github.com/pythonpfin",size="large", icon_image='img/EMPRESA.png')

  
    list_tickers =  pd.read_csv('ticker.csv')
    tickers = st.multiselect(label='Selecione ticker',options=list_tickers,placeholder='Ticker')
    tickers = [tc+'.SA' for tc in tickers]
    
    start_date = st.date_input("De", format="DD/MM/YYYY", value=datetime(2020,1,2))
    end_date = st.date_input("Até", format="DD/MM/YYYY", value="today")

    with st.sidebar.expander('Sobre'):
        st.write('Feito com Carinho ')
        st.markdown("- Roberto Carlos Ricci")
        st.markdown("- Python para finanças")
        st.markdown("- <a href='https://bit.ly/lirobertocarlosricci' target='_blank'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' style='border-radius: 50%; width: 40px; height: 40px;' target='_blank'> </a> ", unsafe_allow_html=True)
    if tickers:
        prices = yf.download(tickers,start=start_date,end=end_date)['Close']

        #retirar o .SA
        prices.columns = prices.columns.str.rstrip('.SA')
        #baixar cotação indice bovespa para comparar 
        prices['IBOV'] = yf.download("^BVSP",start=start_date,end=end_date)['Close']
          # adicionado reggra para excluir o ticker que não conter cotação
        prices = prices.dropna(axis=1, how='any') 
        
        return tickers,prices
    
    return None,None



def main(prices):
  
    #pegar a listagem de colunas e transformar em list, excluido o IBOV, pois vai servir de comparação.
    lst_ticker = list(prices.columns)
    #remover a coluna IBOV  da lista
    lst_ticker.remove('IBOV')
   
    #variavel de peso iguais 
    #calcular pesos iguais utilizando as colunas do dataframe

    weigths = np.ones(len(lst_ticker))/len(lst_ticker)
    #multiplicar 
    #excluir ibov para ficar igual os matrizes
    prices['Portifolio'] = prices.drop("IBOV",axis=1) @ weigths
    #criar uma nova colunas com os valores normalizados
    norm_price  = 100 * prices / prices.iloc[0]

    returns  = prices.pct_change(fill_method=None)[1:]
    #calcular a vol anualizadas
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
            cA.image("img/Portifolio.png")
        elif t == "IBOV":
            cA.image("img/IBOV.png")
        else:
            cA.image(f'https://raw.githubusercontent.com/pythonpfin/icon-b3/main/icon/{t}.png', width=50)

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



if __name__ == "__main__":

    with st.sidebar:
        tickers, prices = sidebar() 
    
    if tickers:
        main(prices)



    