import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Campeonatos",
    page_icon="🏃",
    layout="wide"
)

df_data = pd.read_csv("datasets\_futbol_argentino_logos.csv", index_col=0)

df_data = st.session_state["data"]

# Compruebe si la 'key' ya existe en session_state
# Si no esta, inicialízalo.
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Updates
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

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
df_1 = df_data["Equipo"].unique()
df_1_1 = sorted(df_1)
slb_1 = st.sidebar.selectbox('Equipo', df_1_1)
# filter out data
df_data = df_data[(df_data["Equipo"] == slb_1)]

# feature_2 filters
df_2 = df_data["Año"].unique()
df_2_1 = sorted(df_2)
slb_2 = st.sidebar.selectbox('Año', df_2_1)
# filter out data
df_data = df_data[(df_data["Año"] == slb_2)]

# feature_3 filters
df_3 = df_data["Campeonato"].unique()
slb_3 = st.sidebar.selectbox('Campeonato', df_3)
# filter out data
df_data = df_data[(df_data["Campeonato"] == slb_3)]

torneo_df = df_data[df_data["Campeonato"] == slb_3].iloc[0]

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
