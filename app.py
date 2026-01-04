import streamlit as st

st.set_page_config(layout="wide")

# -------------------------------
# STYLE
# 1. Sistema de cores
# 2. Estrutura (container, layout)
# 3. Superfícies (card, blocos)
# 4. Tipografia
# 5. Componentes específicos
# -------------------------------

st.markdown("""
<style>

/*  -------------------------------
    2. ESTRUTURA
    Define xxx
    ------------------------------- */
    
.container {
  max-width:1200px;
  margin: 0 auto;
}

/*  -------------------------------
    3. SUPERFÍCIES
    Define xxx
    ------------------------------- */

.card {
  background: #161B22;
  padding: 24px;
  border-radius: 0px;
  margin-bottom: 16px;
}

/*  -------------------------------
    4. TIPOGRAFIA GLOBAL
    Define hierarquia de leitura
    ------------------------------- */
   
h1 {
  font-size: 32px;
  margin-bottom: 24px;
}

h2 {
  font-size: 20px;
  margin-bottom: 8px;
}

p {
  font-size: 14px;
  line-height: 1.5;
}

strong {
  font-weight: 600;
}

.card h2 {
  margin-bottom: 8px;
}

.card p {
  margin-bottom: 16px;
}

:root {
  --text: #E6EDF3;
  --muted: #8B949E;
}

p {
  color: var(--muted);
}

h1, h2 {
  color: var(--text);  
}

.kpi-value {
  font-size: 32px;
  font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.title("Dashboard Base")

col1, col2 = st.columns(2)

with col1:
  st.markdown("""
  <div class="card">
    <h2>Indicador A</h2>
    <div class="kpi-value">42</div>
    <p>+3 mês anterior </p>
  </div>
  """, unsafe_allow_html=True)

with col2:
  st.markdown("""
  <div class= "card">
    <h2>Indicador B</h2>
    <div class="kpi-value">17</div>
    <p>+3 mês anterior </p>
  </div>
  """, unsafe_allow_html=True)



st.markdown('</div>', unsafe_allow_html=True)
