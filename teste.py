import streamlit as st

st.title('Teste ECMI 2')
st.write("Sejam Bem Vindos ao aplicativo mais inovador!")
from PIL import Image

# Você pode passar o caminho direto como string
st.image("caminho/para/sua/foto.jpg", caption="Legenda da Imagem")

# Ou abrir com a biblioteca PIL (recomendado para manipulações)
image = Image.open('foto.jpg')
st.image(image, caption='Minha foto local', use_container_width=True)
