import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.container {
  max-width:1200px;
  margin: 0 auto;
}

.card {
  background: #161B22;
  padding: 24px;
  border-radius: 12px;
  margin-bottom: 16px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.title("Dashboard Base")

col1, col2 = st.columns(2)

with col1:
  st.markdown('<div class = "card">', unsafe_allow_html=True)
  st.metric("Indicador A", "42")
  st.markdown('</div>', unsafe_allow_html=True)

with col2:
  st.markdown('<div class = "card">', unsafe_allow_html=True)
  st.metric("Indicador B", "17")
  st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
