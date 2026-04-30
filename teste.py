import streamlit as st
st.title('You to know')
st.write("Seja bem vindo ao mais novo aplicativo que analisa a estrutura da rede social, youtube, na era digital!")
from PIL import Image

# Você pode passar o caminho direto como string
st.image("https://gkpb.com.br/wp-content/uploads/2017/08/novo-logo-youtube.jpg", caption="Primeira rede social que permitiu a atuação do audiovisual na internet")

nome = st.text_input("Antes de comerçamos, escreva seu nome:")
if nome:
     st.write(nome, 'muito bem!Iremos agora conduzir para a criação da biblioteca.')

