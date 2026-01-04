import streamlit as st

# =========================================================
# 1. CONFIGURAÇÃO DO LAYOUT
# =========================================================

st.set_page_config(layout="wide")

# =========================================================
# 2. FONTE DE DADOS
# =========================================================

def load_indicadores():
    """
    Fonte de dados dos indicadores.
    Hoje: lista mockada
    Futuro: query SQL, API, dataframe, etc.
    """
    return [
        {"id": "A", "titulo": "Indicador A", "valor": 42, "delta": "+3 mês anterior", "variant": "default"},
        {"id": "B", "titulo": "Indicador B", "valor": 17, "delta": "estável",           "variant": "default"},
        {"id": "C", "titulo": "Indicador C", "valor": 9,  "delta": "-1 mês anterior",    "variant": "default"},
        {"id": "D", "titulo": "Indicador D", "valor": 63, "delta": "+5 mês anterior",    "variant": "dark"},
        {"id": "E", "titulo": "Indicador E", "valor": 28, "delta": "+1 mês anterior",    "variant": "default"},
        {"id": "F", "titulo": "Indicador F", "valor": 51, "delta": "estável",            "variant": "default"},
    ]

# =========================================================
# 3. DATAPREP
# =========================================================

def get_indicadores():
    """
    Camada intermediária: regras de negócio, cálculos, filtros etc.
    """
    return load_indicadores()

# =========================================================
# 4. STYLE - DESIGN SYSTEM
# =========================================================

st.markdown("""
<style>

/* =======================
   SISTEMA DE CORES
   ======================= */
:root {
  --color-primary: #FF6200;
  --color-primary-soft: #F28500;
  --color-brand-dark: #020F3C;

  --color-black: #000000;
  --color-white: #FFFFFF;

  --gray-100: #EEEEEE;
  --gray-300: #BDBDBD;
  --gray-500: #757575;
  --gray-700: #424242;
  --gray-900: #212121;

  --text-primary: var(--color-black);
  --text-secondary: var(--gray-500);
  --text-inverse: var(--color-white);

  --bg-page: var(--gray-100);
  --bg-card: var(--color-white);

  --accent: var(--color-primary);
  --accent-on-dark: var(--color-white);
}

/* =======================
   BASE DA PÁGINA
   ======================= */
body {
  background: var(--bg-page);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
}

/* =======================
   CARDS - CAIXAS
   ======================= */
.card {
  background: var(--bg-card);
  padding: 40px;
  border-radius: 20px;
  border: 1px solid var(--gray-300);
  margin-bottom: 16px;
}

.card-dark {
  background: var(--color-black);
  border-color: var(--color-black);
}

.card-dark h2,
.card-dark p {
  color: var(--text-inverse);
}

/* =======================
   TIPOGRAFIA
   ======================= */
h1 {
  font-size: 32px;
  margin-bottom: 32px;
}

h2 {
  font-size: 20px;
  font-weight: 400;
  letter-spacing: 0.02em;
  margin-bottom: 8px;
}

p {
  font-size: 14px;
  line-height: 1.5;
  color: var(--text-secondary);
}

.kpi-value {
  font-size: 32px;
  font-weight: 700;
  color: var(--accent);
}

.card-dark .kpi-value {
  color: var(--accent-on-dark);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 5. COMPONENTE VISUAL
# =========================================================

def kpi_card(indicador):
    """
    Renderiza um card de KPI a partir de um dicionário de dados.
    """
    classes = "card"
    if indicador["variant"] == "dark":
        classes += " card-dark"

    return f"""
    <div class="{classes}">
      <h2>{indicador["titulo"]}</h2>
      <div class="kpi-value">{indicador["valor"]}</div>
      <p>{indicador["delta"]}</p>
    </div>
    """

# =========================================================
# 6. LAYOUT
# =========================================================

indicadores = get_indicadores()

st.markdown('<div class="container">', unsafe_allow_html=True)

st.title("Calculadora de Rentabilidade")

# ===== LINHA 1: A B C =====
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(kpi_card(indicadores[0]), unsafe_allow_html=True)

with col2:
    st.markdown(kpi_card(indicadores[1]), unsafe_allow_html=True)

with col3:
    st.markdown(kpi_card(indicadores[2]), unsafe_allow_html=True)

# ===== LINHA 2: D E F =====
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(kpi_card(indicadores[3]), unsafe_allow_html=True)

with col5:
    st.markdown(kpi_card(indicadores[4]), unsafe_allow_html=True)

with col6:
    st.markdown(kpi_card(indicadores[5]), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
