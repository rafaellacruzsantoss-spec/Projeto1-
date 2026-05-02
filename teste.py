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
autor_para_buscar = st.text_input("Digite o nome do autor:")
# 2. Só executa se a variável não estiver vazia
if autor_para_buscar:
    url = f"https://www.goodreads.com?q={autor_para_buscar.replace(' ', '+')}"
    st.write(f"### 🔗 Link de busca para: {autor_para_buscar}")
    st.link_button("Ver no Goodreads, {url}")
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Como não tem classe, vamos buscar todos os títulos h3 (comum em buscas)
        titulos_encontrados = soup.find_all("h3")

        st.write(f"### Resultados para: {autor_para_buscar}")
        
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
 st.write(f"📖 {livro['titulo']} — escrito por: *{livro['autor']}")



  







