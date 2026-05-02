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

# Configurações iniciais
st.title("📚 Explorador de Livros")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11"}

# 1. Primeiro você cria o input
import streamlit as st

# 1. Capture o input do usuário primeiro
autor_input = st.text_input("Digite o nome do autor:")

# 2. Só processe a URL se o usuário tiver digitado algo
if autor_input:
    # Formatamos o texto para a URL (substituindo espaços por +)
    autor_formatado = autor_input.strip().replace(" ", "+")
    
    # URL correta de busca do Goodreads
    url = f"https://www.goodreads.com/search?q={autor_formatado}"
    st.write(f"Clique abaixo para ver os livros de **{autor_input}**:")
   
else:
    st.info("Aguardando você digitar um autor para gerar o link...")
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Como não tem classe, vamos buscar todos os títulos h3 (comum em buscas)
        titulos_encontrados = soup.find_all("h3")

        st.write(f"### Resultados para: {autor_input}")
        
        if titulos_encontrados:
            # Mostra os 3 primeiros resultados
            for item in titulos_encontrados[:3]:
                texto = item.text.strip()
                # Filtramos para não mostrar coisas que não são livros (como 'Vídeos' ou 'Imagens')
                if len(texto) > 3:
                    st.success(f"📖 {texto}")
        else:
            st.warning("Não encontrei títulos específicos no momento.")
            
    else:
        st.error(f"Erro ao conectar: {response.status_code}")
except Exception as e:
    st.error(f"Ocorreu um erro: {e}")




  







