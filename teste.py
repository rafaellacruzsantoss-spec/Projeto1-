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
url = "https://www.amazon.com.br/b?ie=UTF8&node=203733243011" 

# 3. A CONEXÃO (A linha que está faltando!)
# Ela "baixa" o site e guarda tudo dentro da palavra 'response'
response = requests.get(url, headers=headers)
#4 O status 200 que você recebeu veio daqui:
st.write(f"Status: {response.status_code}")

# Agora transformamos o conteúdo em algo "legível" para o Python
soup = BeautifulSoup(response.content, "html.parser")

# Exemplo: Pegar o texto de uma div que tem a classe 'autor'
elemento = soup.find("div", {"class": "autor"})

if elemento:
    st.subheader("Informação encontrada:")
    st.write(elemento.text) # Mostra o texto que está dentro da div
else:
    st.warning("Conectei ao site, mas não encontrei o que você procurou.")
# 5. Criar a "sopa" para ler o HTML
soup = BeautifulSoup(response.content, "html.parser")
# 6. Procurar o que você quer
elemento = soup.find("div", {"stactiText": "Livros"})
# Supondo que os títulos estejam em tags <h3> e autores em <span>
titulos = soup.find_all("h3")
autores = soup.find_all("span")

# Vamos criar uma lista para guardar os dados
biblioteca = []

# O zip combina as duas listas: o primeiro título com o primeiro autor, etc.
for t, a in zip(titulos, autores):
    biblioteca.append({
        "titulo": t.text.strip(),
        "autor": a.text.strip()
    })

# Agora mostramos no Streamlit
for livro in biblioteca[:5]: # Mostra os 5 primeiros
    st.write(f"📖 **{livro['titulo']}** — escrito por: *{livro['autor']}*")



  







