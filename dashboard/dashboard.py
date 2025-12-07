import streamlit as st
import pandas as pd
import plotly.express as px

# ============================
#   CONFIGURAÇÕES DO APP
# ============================
st.set_page_config(
    page_title="Monitor Mercado Livre",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Monitor de Preços - Mercado Livre")
st.markdown("Dashboard automatizado baseado no ETL do Mercado Livre.")

# ============================
#   CARREGAR DADOS
# ============================
@st.cache_data
def load_data():
    return pd.read_json("../data/produtos.json")

df = load_data()


# ============================
#   FILTROS LATERAIS
# ============================
st.sidebar.header("Filtros")

marcas = st.sidebar.multiselect(
    "Marca", 
    options=df["marca"].dropna().unique(),
    default=df["marca"].dropna().unique()
)

preco_min, preco_max = st.sidebar.slider(
    "Faixa de preço (novo)",
    0.0,
    float(df["preco_novo"].max()),
    (0.0, float(df["preco_novo"].max()))
)

df_filtered = df[
    (df["marca"].isin(marcas)) &
    (df["preco_novo"] >= preco_min) &
    (df["preco_novo"] <= preco_max)
]


# ============================
#   KPIs / MÉTRICAS
# ============================
col1, col2, col3 = st.columns(3)

col1.metric("Total de produtos", len(df_filtered))
col2.metric("Preço médio", f"R$ {df_filtered['preco_novo'].mean():.2f}")
col3.metric("Maior desconto", df_filtered["desconto"].fillna("0").max())


# ============================
#   TABELA DE RESULTADOS
# ============================
st.subheader("📋 Lista de Produtos")
st.dataframe(df_filtered, use_container_width=True)


# ============================
#   GRÁFICO DE PREÇOS
# ============================
st.subheader("📈 Distribuição de Preços")

fig = px.histogram(
    df_filtered,
    x="preco_novo",
    nbins=30,
    title="Distribuição dos preços novos",
    color="marca"
)
st.plotly_chart(fig, use_container_width=True)


# ============================
#   MAIORES DESCONTOS
# ============================
st.subheader("🔥 TOP 10 MAIORES DESCONTOS")

df_top = df_filtered.copy()
df_top["perc_desc"] = df_top["desconto"].str.replace("% OFF", "").astype(float)
df_top = df_top.sort_values(by="perc_desc", ascending=False).head(10)

st.table(df_top[["descricao", "marca", "preco_novo", "preco_antigo", "desconto", "link"]])
