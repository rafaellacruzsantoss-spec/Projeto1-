import streamlit as st

st.title('')
st.write('Nas ondas das inspirações')
st.write("Seja bem vindo ao aplicativo mais inovador!")

st.image("https://lens.usercontent.google.com/image?vsrid=CJ6VsYmKx8vZNBACGAEiJGNkNWUzZDhiLTcwNTYtNGUzYy05NDNkLTgyYWYwOTFhZjU1OTJ7IgJjZigNQnMKLmxmZS1kdW1teToxOGVjNDlkOS0xNTAwLTRjY2QtYWVmNi0zMGM0Y2U0YjI4ZDESQQo_L2Jucy9jZi9ib3JnL2NmL2Jucy9sZW5zLWZyb250ZW5kLWFwaS9wcm9kLmxlbnMtZnJvbnRlbmQtYXBpLzUwONjdvsKik5QD&gsessionid=8SRQZQFX9isdrN1mjd661oIherkd6NfWi26BlRE85y6pyc6-xQFEBg", width=200)
from PIL import Image

# Você pode passar o caminho direto como string
st.image("https://cdn-ileapbh.nitrocdn.com/awswdmxduTjCKQiPPVuNWTjlobpOKWLT/assets/images/optimized/rev-3155ec0/aguiarbuenosaires.com/wp-content/uploads/2022/03/livraria-ateneo.jpg", caption="El Ateneo, uma das livrarias mais belas do mundo")

nome = st.text_input("Digite um lugar que te inspire")
if nome:
     st.write(nome, 'parece ser incrível')

