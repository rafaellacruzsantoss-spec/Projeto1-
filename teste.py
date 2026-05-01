import streamlit as st
st.title('Guia de Livros ')
st.write("Seja bem vindo ao mais novo aplicativo que ajudará a você estar mais conectado com pautas literárias!")
from PIL import Image
nome = st.text_input("Antes de comerçamos, escreva seu nome:")
if nome:
 st.write(nome,', muito bem! Agora iremos conduzir você para a criação da sua biblioteca.')
# Você pode passar o caminho direto como string
 st.image("https://offloadmedia.feverup.com/riodejaneirosecreto.com/wp-content/uploads/2023/04/13070413/Real-Gabinete-Portugues.jpg", caption="Real Gabinete português de Leitura, Rio de Janeiro")
 st.write("De início, é possível notar a extrema importância que a literatura exerce no papel de construção de cada individuo na sociedade. Assim, esse aplicativo busca informar e incentivar o consumo literario baseado em dicas para a permanência dessa prática no seu cotidiano.")
 import streamlit as st
import requests
from bs4 import BeautifulSoup

# 1. Identidade (O que já corrigimos antes)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11"}

# 2. O Endereço (Coloque o site que você quer aqui)
url = "https://www.google.com" 

# 3. A CONEXÃO (A linha que está faltando!)
# Ela "baixa" o site e guarda tudo dentro da palavra 'response'
response = requests.get(url, headers=headers)

# 4. Mostrar o resultado no Streamlit
st.write(f"Status da conexão: {response.status_code}")

# 5. Criar a "sopa" para ler o HTML
soup = BeautifulSoup(response.content, "html.parser")

# 6. Procurar o que você quer
elemento = soup.find("div", {"class": "nome do livro"})

if elemento:
    st.write(elemento.text)
else:
    st.write("Não encontrei a classe 'nome do livro' nesse site.")

  







