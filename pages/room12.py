import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser
from time import sleep

# Configuração inicial da página

st.set_page_config(page_title="Sistema de Votação com Gráfico", layout="centered")

# Títulos e descrição
st.title("🗳️ Sistema de Votação")
st.write("Vote com cuidado! Veja com atenção o discurso de cada um, e então vote. Você só pode votar uma vez!")

# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou

col1, col2 = st.columns(2)

with col1:
    if st.button("Discurso do candidato 1"):
        webbrowser.open("https://drive.google.com/file/d/1d6C5kr-OL-gTC2oohPFOAQbGqg4Sj4ae/view")
with col2:
        if st.button("Discurso do candidato 2"):
            webbrowser.open("https://drive.google.com/file/d/1O3CyhZLgpj_WDgSwf0rhnEnNIda29eiL/view")

if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:
    # Botões de votação
    col3, col4 = st.columns(2)

    with col3:
        if st.button("Votar no Candidato 1"):  
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
    with col4:
        if st.button("Votar no Candidato 2"):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")
            
col5, col6 = st.columns(2)
with col5:
    st.image("data:image/jpeg;base64,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", width=160)
with col6:
    st.image("https://media.tenor.com/MjhAx0N2-rcAAAAe/aff-é-suco-de-caju.png", width=160)

if st.button("Ver resultado"):
    st.success("Transferindo")
    sleep(0.5)
    st.switch_page("pages/resultado.py")

import base64

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def cadastro():
    background_image_path = "img/fundo3.jpeg"  # Certifique-se de que o caminho está correto
    background_image = get_base64_image(background_image_path)

    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{background_image}"); 
            background-size: cover;
            background-position: center; 
            background-attachment: fixed; 
        }}
    </style>
    """, unsafe_allow_html=True)


st.sidebar.image("img/vote.jpeg")
# Chamada da função para carregar o fundo
cadastro()

def ver_preenchidos(campos):
    return all(campos.values())
