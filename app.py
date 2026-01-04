import streamlit as st
import pandas as pd
import altair as alt

# =========================================================
# 0. DESIGN TOKENS
# =========================================================

color_black = "#000000"
color_white = "#ffffff"
color_accent = "#ff6200"

gray_300 = "#bdbdbd"
gray_500 = "#757575"

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
    """
    return [
        {"id": "A", "titulo": "Indicador A", "valor": 42, "delta": "+3 mês anterior", "variant": "default"},
        {"id": "B", "titulo": "Indicador B", "valor": 17, "delta": "estável", "variant": "default"},
        {"id": "C", "titulo": "Indicador C", "valor": 9,  "delta": "-1 mês anterior", "variant": "default"},
        {"id": "D", "titulo": "Indicador D", "valor": 63, "delta": "+5 mês anterior", "variant": "dark"},
        {"id": "E", "titulo": "Indicador E", "valor": 28, "delta": "+1 mês anterior", "variant": "default"},
        {"id": "F", "titulo": "Indicador F", "valor": 51, "delta": "estável", "variant": "default"},
        {
            "id": "G",
            "titulo": "Indicador G",
            "valor": "Total",
            "delta": "atenção: valor abaixo da projeção",
            "variant": "dark",
            "span": "full",
            "series": [12, 18, 15, 22, 19, 25, 23],
        },
    ]

# =========================================================
# 3. DATAPREP
# =========================================================

def get_indicadores():
    return load_indicadores()

# =========================================================
# 4. STYLE
# =========================================================

st.markdown(f"""
<style>
:root {{
  --color-black: {color_black};
  --color-white: {color_white};
  --accent: {color_accent};
  --gray-300: {gray_300};
  --gray-500: {gray_500};
}}

body {{
  background: var(--color-black);
}}

.container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
}}

.card {{
  background: var(--color-white);
  padding: 40px;
  border-radius: 20px;
  border: 1px solid var(--gray-300);
  margin-bottom: 16px;
}}

.card-dark {{
  background: var(--color-black);
  border-color: var(--color-black);
}}

.card-dark h2,
.card-dark p {{
  color: var(--color-white);
}}

h1 {{
  font-size: 32px;
  margin-bottom: 80px;
}}

h2 {{
  font-size: 20px;
  font-weight: 400;
  letter-spacing: 0.02em;
  margin-bottom: 8px;
}}

p {{
  font-size: 14px;
  line-height: 1.5;
  color: var(--gray-500);
}}

.kpi-value {{
  font-size: 50px;
  font-weight: 700;
  color: var(--accent);
}}

.card-dark .kpi-value {{
  color: var(--color-white);
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 5. COMPONENTES
# =========================================================

def kpi_card(indicador):
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

def line_chart_black(series):
    df = pd.DataFrame({
        "x": list(range(len(series))),
        "y": series
    })

    base = alt.Chart(df).encode(
        x=alt.X(
            "x:O",
            title=None,
            axis=alt.Axis(
                labelColor=color_black,
                tickColor=color_black,
                labelAngle=0
            )
        ),
        y=alt.Y(
            "y:Q",
            title=None,
            axis=alt.Axis(
                labels=False,
                ticks=False
            )
        )
    )

    line = base.mark_line(color=color_black, strokeWidth=2)
    points = base.mark_point(color=color_black, filled=True, size=60)
    labels = base.mark_text(
        dy=-10,
        color=color_black,
        fontSize=12
    ).encode(text="y:Q")

    return (line + points + labels).properties(
        height=160,
        background=color_white
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        grid=False
    )

# =========================================================
# 6. LAYOUT – GRID DINÂMICO
# =========================================================

indicadores = get_indicadores()
num_colunas = 3

st.markdown('<div class="container">', unsafe_allow_html=True)
st.title("Calculadora de Rentabilidade")

for i in range(0, len(indicadores), num_colunas):
    linha = indicadores[i:i + num_colunas]

    # Caso full-width (Indicador G)
    if len(linha) == 1 and linha[0].get("span") == "full":
        indicador = linha[0]
        col = st.columns(1)[0]

        with col:
            st.markdown(
                f"""
                <div class="card card-dark">
                  <h2>{indicador["titulo"]}</h2>
                  <div class="kpi-value">{indicador["valor"]}</div>
                  <p>{indicador["delta"]}</p>
                """,
                unsafe_allow_html=True
            )

            st.altair_chart(
                line_chart_black(indicador["series"]),
                use_container_width=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        continue

    # Grid normal
    cols = st.columns(num_colunas)
    for col, indicador in zip(cols, linha):
        with col:
            st.markdown(kpi_card(indicador), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
