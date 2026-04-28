import streamlit as st

st.title('DIVA')
st.write("Seja Bem Vindo ao aplicativo mais inovador!")

st.image("https://img.elo7.com.br/product/zoom/3559173/placas-boas-vindas-recepcao-casamento.jpg", width=200)
from PIL import Image

# Você pode passar o caminho direto como string
st.image("https://cdn-ileapbh.nitrocdn.com/awswdmxduTjCKQiPPVuNWTjlobpOKWLT/assets/images/optimized/rev-3155ec0/aguiarbuenosaires.com/wp-content/uploads/2022/03/livraria-ateneo.jpg", caption="El Ateneo, uma das livrarias mais belas do mundo")

nome = st.text_input("Digite seu nome")
if nome:
     st.write(nome, 'é um cara legal')

