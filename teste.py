import streamlit as st
st.title('Guia de Livros ')
st.write("Seja bem vindo ao mais novo aplicativo que ajudará a você estar mais conectado com pautas literárias!")
from PIL import Image
nome = st.text_input("Antes de comerçamos, escreva seu nome:")
if nome:
 st.write(nome,', muito bem! Agora iremos conduzir você para a criação da sua biblioteca.')
# Você pode passar o caminho direto como string
 st.image("https://offloadmedia.feverup.com/riodejaneirosecreto.com/wp-content/uploads/2023/04/13070413/Real-Gabinete-Portugues.jpg", caption="Real Gabinete português de Leitura, Rio de Janeiro")
 st.write("De início, é possível notar a extrema importância que a literatura exerce no papel de construção de cada individuo na sociedade. Assim, esse aplicativo busca incentivar o consumo literario critico baseado na revista The New York Times.")
import requests
from bs4 import BeautifulSoup
resposta = requests.get("https://api.nytimes.com/svc/books/v3/lists/{date}/{list}.json")
dados = resposta.json()
soup = BeautifulSoup (site.content)
lista = soup.find_all("author",["weeks_on_list": "title"])






