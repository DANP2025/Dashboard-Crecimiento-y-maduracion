import streamlit as st

# -------------------------------
# Configuración general de la app
# -------------------------------
st.set_page_config(
    page_title="Perfil de crecimiento y maduración",
    layout="wide"
)

# -----------------------------------------
# Ocultar menú, header y footer de Streamlit
# -----------------------------------------
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Título (opcional, estético)
# -------------------------------
st.markdown(
    "<h2 style='text-align: center;'>Perfil de crecimiento y maduración del deportista</h2>",
    unsafe_allow_html=True
)

# -------------------------------
# Power BI embebido
# -------------------------------
st.markdown(
    """
    <iframe 
        title="Plantilla crecimiento y maduracion"
        width="100%" 
        height="900"
        src="https://app.powerbi.com/view?r=eyJrIjoiMDVhN2VjYWEtYjY3NS00NmExLTk3MmQtMjg0Y2VmNGNiYzc4IiwidCI6IjY4NTNhNzY1LWEzN2MtNGFmOS05MDkwLWU2N2Q2N2FlZWNhZCIsImMiOjR9"
        frameborder="0"
        allowFullScreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
