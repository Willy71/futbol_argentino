import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Campeonatos",
    page_icon="🏃",
    layout="wide"
)

# Check if you've already initialized the data
if 'df' not in st.session_state:
    # Get the data if you haven't
    df = pd.read_csv('datasets/futbol_argentino_logos.csv')
    # Save the data to session state
    st.session_state.df = df

# Retrieve the data from session state
df = st.session_state.df
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


# feature_1 filters
df_1 = df["Año"].unique()
slb_1 = st.sidebar.selectbox('Año', df_1)
# filter out data
df = df[(df["Año"] == slb_1)]

# feature_2 filters
df_2 = df["Campeonato"].unique()
slb_2 = st.sidebar.selectbox('Campeonato', df_2)
# filter out data
df = df[(df["Campeonato"] == slb_2)]

# feature_3 filters
df_3 = df["Equipo"].unique()
slb_3 = st.sidebar.selectbox('Equipo', df_3)
# filter out data
df = df[(df["Equipo"] == slb_3)]

torneo_df = df[df["Equipo"] == slb_3].iloc[0]

centrar_texto(torneo_df['Equipo'], 4, "white")
centrar_imagen(torneo_df['Logo'], 100)

st.title('')

centrar_texto(f"Puntos: {torneo_df['Puntos']}", 6, "white")
centrar_texto(f"Ganados: {torneo_df['Ganados']}", 6, "white")
centrar_texto(f"Perdidos: {torneo_df['Perdidos']}", 6, "white")
centrar_texto(f"Empatados: {torneo_df['Empatados']}", 6, "white")
centrar_texto(f"Partidos: {torneo_df['Partidos Jugados']}", 6, "white")
centrar_texto(f"Goles a favor: {torneo_df['GF']}", 6, "white")
centrar_texto(f"Goles en contra: {torneo_df['GC']}", 6, "white")
centrar_texto(f"Diferencia: {torneo_df['DIF']}", 6, "white")
