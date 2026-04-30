import streamlit as st
st.title('To be read')
st.write("Seja bem vindo ao mais novo aplicativo que tem como intuito encontrar a sua versão literária!")
from PIL import Image

# Você pode passar o caminho direto como string
st.image("https://cdn-ileapbh.nitrocdn.com/awswdmxduTjCKQiPPVuNWTjlobpOKWLT/assets/images/optimized/rev-3155ec0/aguiarbuenosaires.com/wp-content/uploads/2022/03/livraria-ateneo.jpg", caption="El Ateneo, uma das livrarias mais belas do mundo")

nome = st.text_input("Antes de comerçamos, escreva seu nome:")
if nome:
     st.write(nome, 'muito bem!Iremos agora conduzir para a criação da biblioteca.')

