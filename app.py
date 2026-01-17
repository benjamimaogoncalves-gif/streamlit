# =========================================================
# 0. BIBLIOTECAS | LIBRARIES
# =========================================================

import streamlit as st
import pandas as pd

# =========================================================
# 1. DESIGN
# =========================================================

# 1.A. SISTEMA DE CORES | COLOR SYSTEM
# configurar as cores padrão escolhidas | configure the default colors chosen

color_black = "#000000"
color_white = "#ffffff"
color_accent = "#ff6200"
gray_300 = "#bdbdbd"
gray_500 = "#757575"

# 1.B. LAYOUT
# ajustar a configuração padrão da página | configure the default settings of the page

itau_logo_completo_laranja = st.image(Path="https://i0.wp.com/assets.b9.com.br/wp-content/uploads/2023/12/itau-nova-marca.png?fit=1920%2C1080&ssl=1")
itau_logo_laranja = st.image(Path="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Ita%C3%BA_Unibanco_logo_2023.svg/500px-Ita%C3%BA_Unibanco_logo_2023.svg.png")
itau_home = "https://www.itau.com.br/"

st.set_page_config(
    page_title="Calculadora de Rentabilidade",
    layout="wide",
    initial_sidebar_state="auto",
#     image = itau_logo_completo_laranja
)
