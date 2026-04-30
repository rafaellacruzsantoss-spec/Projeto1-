import streamlit as st
st.title('You to know')
st.write("Seja bem vindo ao mais novo aplicativo que analisa a estrutura da rede social, youtube, na era digital!")
from PIL import Image

# Você pode passar o caminho direto como string
st.image("https://gkpb.com.br/wp-content/uploads/2017/08/novo-logo-youtube.jpg", caption="Primeira rede social que permitiu a atuação do audiovisual na internet")

nome = st.text_input("Antes de comerçamos, escreva seu nome:")
if nome:
     st.write(nome, ', muito bem!Agora iremos conduzir para a criação da biblioteca.')

# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# https://requests.readthedocs.io/en/master/user/install/#install

import requests

def execute():
  requestUrl = "https://api.nytimes.com/svc/books/v3/lists/[DATE]/[LIST].json?api-key=[YOUR_API_KEY]"
  requestHeaders = {
    "Accept": "application/json"
  }

  response = requests.get(requestUrl, headers=requestHeaders)

  print(response.text)

if __name__ == "__main__":
  execute()
