import streamlit as st

st.set_page_config(layout="wide")

# =========================================================
# STYLE
# 1. Sistema de cores
# 2. Estrutura
# 3. Superfícies
# 4. Tipografia
# 5. Componentes
# =========================================================

st.markdown("""
<style>

/* =========================================================
   1. SISTEMA DE CORES (TOKENS SEMÂNTICOS)
   ========================================================= */

:root {
  /* Identidade */
  --color-primary: #FF6200;
  --color-primary-soft: #F28500;
  --color-brand-dark: #020F3C;

  /* Neutros */
  --color-black: #000000;
  --color-white: #FFFFFF;

  /* Escala de cinza */
  --gray-100: #EEEEEE;
  --gray-300: #BDBDBD;
  --gray-500: #757575;
  --gray-700: #424242;
  --gray-900: #212121;

  /* Texto */
  --text-primary: var(--color-black);
  --text-secondary: var(--gray-500);
  --text-inverse: var(--color-white);

  /* Backgrounds */
  --bg-page: var(--gray-100);
  --bg-card: var(--color-white);

  /* Destaques */
  --accent: var(--color-primary);
  --accent-dark: var(--color-white);
  --accent-soft: var(--color-primary-soft);
}

/* =========================================================
   2. ESTRUTURA
   ========================================================= */

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  /* background removido */
}

/* =========================================================
   3. SUPERFÍCIES
   ========================================================= */

.card {
  background: var(--bg-card);
  padding: 40px;
  border-radius: 20px;
  margin-bottom: 16px;
  border: 1px solid var(--gray-300);
}

.card-dark {
  background: var(--color-black);
  border: 1px solid var(--color-black);
}

.card-dark h2,
.card-dark p {
  color: var(--text-inverse);
}

.card-dark .kpi-value {
  color: var(--accent-dark);
}

/* =========================================================
   4. TIPOGRAFIA GLOBAL
   ========================================================= */

h1 {
  font-size: 32px;
  margin-bottom: 24px;
  color: var(--text-primary);
}

h2 {
  font-size: 20px;
  margin-bottom: 8px;
  color: var(--text-primary);
}

p {
  font-size: 14px;
  line-height: 1.5;
  margin-bottom: 16px;
  color: var(--text-secondary);
}

strong {
  font-weight: 600;
}

/* Tipografia local */

.card h2 {
  font-weight: 400;
  letter-spacing: 0.02em;
}

.card p {
  margin-bottom: 16px;
}

/* =========================================================
   5. COMPONENTES
   ========================================================= */

.kpi-value {
  font-size: 32px;
  font-weight: 700;   /* bold real */
  color: var(--accent);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LAYOUT
# =========================================================

st.markdown('<div class="container">', unsafe_allow_html=True)

st.title("Calculadora Rentabilidade")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
      <h2>Indicador A</h2>
      <div class="kpi-value">42</div>
      <p>+3 mês anterior</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
      <h2>Indicador B</h2>
      <div class="kpi-value">17</div>
      <p>estável</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
      <h2>Indicador C</h2>
      <div class="kpi-value">9</div>
      <p>-1 mês anterior</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card card-dark">
      <h2>Indicador D</h2>
      <div class="kpi-value">63</div>
      <p>+5 mês anterior</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
