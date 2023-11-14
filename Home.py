import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets\_futbol_argentino_logos.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending = False)
    st.session_state["data"] = df_data

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Futbol Argentino",
    page_icon="⚽",
    layout="wide"
)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/430MMcSq/wepik-export-20231112174143b-KKB.jpg");
background-size: 180%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stSidebar"] {{
background: rgba(28,28,56,1);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


def centrar_imagen(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{imagen}" width="{ancho}">'
        f'</div>',
        unsafe_allow_html=True
    )


def centrar_texto(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: center; color: {color}'>{texto}</h{tamanho}>",
                unsafe_allow_html=True)


df_data = pd.read_csv("datasets\_futbol_argentino_logos.csv", index_col=0)
df_logos = pd.read_csv("datasets\_logos_equipos.csv", index_col=0)

centrar_imagen("https://i.postimg.cc/qvb4nYF8/Logo-lpf-afa.png", 100)


# Título centrado en la página
centrar_texto("Futbol Argentino", 1, "white")
centrar_texto("Era profesional 1931-2023", 3, "white")

st.title("")

# st.sidebar.write("PRUEBA")
st.sidebar.markdown("Pagina realizada por Guillermo Cerato")

st.sidebar.markdown(
    "[Base de datos original](https://www.kaggle.com/datasets/ivanramosctes/liga-argentina-1931-2023)")
st.sidebar.markdown(
    "[ETL del proyecto](https://www.kaggle.com/code/willycerato/liga-argentina-de-futbol-analisis-python)")
st.sidebar.title("")
st.sidebar.markdown(
    "[Kaggle Guillermo Cerato](https://www.kaggle.com/willycerato)")
st.sidebar.markdown(
    "[Instagram Guillermo Cerato](https://www.instagram.com/willycerato)")


centrar_texto("El conjunto de datos del futbol profesional argentino, que va desde el año 1931, fecha de inicio de la era profesional, hasta el año actual 2023, fue reestructurado en Kaggle para poder tener goles a favor y en contra por torneo, asi como tambien, los partidos jugados por cada equipo y si ellos fueron ganadores, perdedores o terminaron empatados.", 7, "white")
