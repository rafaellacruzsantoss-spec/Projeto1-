import streamlit as st
st.title('Guia de Livros ')
st.write("Seja bem vindo ao mais novo aplicativo que ajudará a você estar mais conectado com pautas literárias!")
from PIL import Image
nome = st.text_input("Antes de comerçamos, escreva seu nome:")
if nome:
     st.write(nome, ', muito bem!Agora iremos conduzir você para a criação da sua biblioteca.')
# Você pode passar o caminho direto como string
st.image("https://offloadmedia.feverup.com/riodejaneirosecreto.com/wp-content/uploads/2023/04/13070413/Real-Gabinete-Portugues.jpg", caption="Real Gabinete português de Leitura, Rio de Janeiro")
st.write("De início, é possível notar a extrema importancia que a literatura exerce no papel de construção de cada individuo na sociedade. Assim, esse aplicativo busca incentivar não só a leitura mas as consequências que um bom livro pode oferecer")
import os
from dotenv import load_dotenv

# Isso procura um arquivo chamado .env no mesmo diretório do script
load_dotenv()
api_key = os.getenv("CHAVE_DA_API")
database_url = os.getenv("DATABASE_URL")

print(f"A chave carregada foi: {api_key}")     


