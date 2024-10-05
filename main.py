# Quando for rodar pela primeira vez instalar
# pip install streamlit yfinance

# Depois que copiar o codigo rodar no terminal
# streamlit run main.py



# importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf



#Criar funções de carregamento de dados
    #Cotações do Itau - ITUB4 - 2010 a 2024
@st.cache_data 
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end = "2024-07-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

acoes = ["ITUB4.SA","ITSA4.SA","PETR4.SA","MGLU3.SA","VALE3.SA","ABEV3.SA","GGBR4.SA"]
dados = carregar_dados(acoes)




# Criar a interface do streamlit
st.write("""

# Preço das Ações
Evolução do preço das ações a partir de 2010


         """)
# Criar Gráfico

lista_acoes = st.multiselect("Escolha as ações para visualizar ",dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica:"Close"})


print(lista_acoes)

st.line_chart(dados)


# Curso de Streamlit - Aula 2 - Filtros e Gráficos