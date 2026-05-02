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
 st.write("Neste aplicativo temos uma página repleta de dicas para iniciantes de liretura como estudo mas também como hobby! Prezamos múltiplas interações de diferentes aspectos da literatura.")
import streamlit as st

# Criando o menu na barra lateral
with st.sidebar:
    st.title("Sugestôes para iniciantes")
    # O selectbox funciona como o seletor do menu
    menu = st.radio(
        "Escolha uma opção:",
        ("Buscar Livros", "Dicas")
    )

# Lógica do Menu
if menu == "Buscar Livros":
    st.header("🔍 Scraper de Livros")
    autor = st.text_input("Digite o autor:")
    # ... aqui vai o seu código de scraping com H3 ...
    if autor:
        st.markdown(f"### 📖 Resultados para {autor}")

elif menu == "Dicas para iniciantes":
    st.write("Para o hábito de ler continuar existindo e se tornar cada vez mais presente no dia a dia, segue dicas para melhorar sua leitura:"
             
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Configurações iniciais
st.title("📚 Explorador de Livros")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11"}

# 1. Capture o input do usuário primeiro
autor_input = st.text_input("Digite o nome do autor para buscar no Goodreads:")

# 2. Só processe a URL se o usuário tiver digitado algo
if autor_input:
    # Formatamos o texto para a URL (substituindo espaços por +)
    autor_formatado = autor_input.strip().replace(" ", "+")
    
    # URL correta de busca do Goodreads
    url = f"https://www.goodreads.com/search?q={autor_formatado}"
 
    st.link_button("Ver no Goodreads", livro['link'])
    
    st.divider()
else:
    st.info("Aguardando você digitar um autor para gerar o link...") 

 


  







