from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME")
SCHEMA = os.getenv("DB_SCHEMA", "public")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# ==========================================================
# ⚙️ FUNÇÕES AUXILIARES
# ==========================================================
@st.cache_resource
def get_engine():
    """Cria e cacheia engine de conexão"""
    return create_engine(DATABASE_URL, pool_pre_ping=True)

@st.cache_data(ttl=300)
def list_tables():
    """Lista tabelas do schema"""
    engine = get_engine()
    insp = inspect(engine)
    return insp.get_table_names(schema=SCHEMA)

@st.cache_data(ttl=300)
def get_columns(table):
    """Retorna colunas de uma tabela"""
    engine = get_engine()
    insp = inspect(engine)
    return [c["name"] for c in insp.get_columns(table, schema=SCHEMA)]

@st.cache_data(ttl=300)
def get_table_date_range(table):
    """Obtém data mínima e máxima da tabela"""
    engine = get_engine()
    q = f'SELECT MIN(date) AS mn, MAX(date) AS mx FROM "{SCHEMA}"."{table}";'
    with engine.connect() as conn:
        row = conn.execute(text(q)).fetchone()
    return row[0], row[1]

def detect_price_column(cols):
    """Detecta coluna de preço por heurística"""
    for k in ["prazo", "a_vista"]:
        for c in cols:
            if k in c.lower():
                return c
    return None

def load_table_data(table, region_filter=None, date_from=None, date_to=None, price_col=None):
    """Carrega dados filtrados de uma tabela"""
    engine = get_engine()
    cols = get_columns(table)

    if "date" not in cols:
        raise ValueError("Tabela não tem coluna 'date'.")

    price_col = price_col or detect_price_column(cols)
    if not price_col:
        raise ValueError("Não foi detectada coluna de preço nesta tabela.")

    region_col = "region_id" if "region_id" in cols else ("region" if "region" in cols else None)
    select_cols = ['id', 'date', f'"{price_col}" AS price']
    if region_col:
        select_cols.append(region_col)
    select_sql = ", ".join(select_cols)

    where = []
    params = {}
    if date_from:
        where.append("date >= :date_from")
        params["date_from"] = date_from
    if date_to:
        where.append("date <= :date_to")
        params["date_to"] = date_to
    if region_filter and region_col:
        where.append(f"{region_col} = :region")
        params["region"] = region_filter

    where_sql = "WHERE " + " AND ".join(where) if where else ""
    query = f'SELECT {select_sql} FROM "{SCHEMA}"."{table}" {where_sql} ORDER BY date;'

    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn, params=params)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

# ==========================================================
# 🎨 INTERFACE STREAMLIT
# ==========================================================
st.set_page_config(layout="wide", page_title="Dashboard de Preços")
st.title("📈 Dashboard de Preços e Tendências")

st.sidebar.header("Filtros")
tables = list_tables()
product = st.sidebar.selectbox("Produto (tabela)", options=sorted(tables))

# Detectar colunas automaticamente
cols = get_columns(product)
price_col = detect_price_column(cols)
if not price_col:
    price_col = st.sidebar.text_input("Coluna de preço", value="price_brl")

region_col = "region_id" if "region_id" in cols else ("region" if "region" in cols else None)

# Obter intervalo de datas
min_date, max_date = get_table_date_range(product)
if not min_date or not max_date:
    st.error("Tabela não contém valores de data válidos.")
    st.stop()

default_start = max_date - timedelta(days=365)
date_range = st.sidebar.date_input("Período", value=(default_start, max_date), min_value=min_date, max_value=max_date)
date_from, date_to = date_range if isinstance(date_range, tuple) else (default_start, max_date)

# Filtro de região
region_filter = None
if region_col:
    q = f'SELECT DISTINCT {region_col} FROM "{SCHEMA}"."{product}" ORDER BY 1 LIMIT 1000;'
    with get_engine().connect() as conn:
        regions = [r[0] for r in conn.execute(text(q)).fetchall() if r[0] is not None]
    regions = ["Todos"] + regions
    sel_region = st.sidebar.selectbox("Região", options=regions)
    if sel_region != "Todos":
        region_filter = sel_region

agg_choice = st.sidebar.selectbox("Agregação de tempo", ["Diário", "Semanal", "Mensal"], index=2)
show_anomalies = st.sidebar.checkbox("Mostrar anomalias", value=True)

# ==========================================================
# 📦 CARREGAR DADOS
# ==========================================================
try:
    df = load_table_data(product, region_filter, date_from, date_to, price_col)
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

if df.empty:
    st.warning("Sem dados para o filtro selecionado.")
    st.stop()

# ==========================================================
# 📊 VISUALIZAÇÕES
# ==========================================================
col1, col2 = st.columns([2, 1])

with col2:
    st.metric("Período", f"{df['date'].min()} → {df['date'].max()}")
    st.metric("Registros", len(df))
    st.metric("Preço médio", f"{df['price'].mean():.2f}")

# --- Série temporal ---
with col1:
    st.subheader("📆 Tendência de Preços")
    df_temp = df.copy()
    df_temp["date"] = pd.to_datetime(df_temp["date"])
    if agg_choice == "Semanal":
        df_temp["period"] = df_temp["date"].dt.to_period("W").apply(lambda r: r.start_time)
    elif agg_choice == "Mensal":
        df_temp["period"] = df_temp["date"].dt.to_period("M").apply(lambda r: r.start_time)
    else:
        df_temp["period"] = df_temp["date"]

    ts = df_temp.groupby("period")["price"].mean().reset_index()
    fig = px.line(ts, x="period", y="price", markers=True, title=f"Preço médio ({agg_choice}) — {product}")
    st.plotly_chart(fig, use_container_width=True)

# --- Boxplot e histograma ---
st.subheader("📦 Distribuição de preços")
fig_box = px.box(df, y="price", points="outliers", title="Boxplot de preços")
fig_hist = px.histogram(df, x="price", nbins=40, title="Histograma de preços")
st.plotly_chart(fig_box, use_container_width=True)
st.plotly_chart(fig_hist, use_container_width=True)

# --- Anomalias ---
if show_anomalies:
    st.subheader("🚨 Anomalias (preços negativos / outliers)")
    q1, q3 = df["price"].quantile(0.25), df["price"].quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    anom = df[(df["price"] < 0) | (df["price"] < low) | (df["price"] > high)]
    if anom.empty:
        st.info("Nenhuma anomalia detectada.")
    else:
        st.dataframe(anom.sort_values("date"), use_container_width=True)
        csv = anom.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Baixar anomalias CSV", csv, f"anomalias_{product}.csv", "text/csv")

# --- Variação mensal (LAG) ---
st.subheader("📉 Variação mensal de preço")
try:
    partition_col = region_col if region_col else None
    q = f"""
    SELECT
        {partition_col or '1 AS dummy'},
        date_trunc('month', date) AS month,
        AVG("{price_col}") AS avg_price,
        LAG(AVG("{price_col}")) OVER (
            {'PARTITION BY ' + partition_col if partition_col else ''}
            ORDER BY date_trunc('month', date)
        ) AS prev_avg,
        ROUND(
            (AVG("{price_col}") - LAG(AVG("{price_col}")) OVER (
                {'PARTITION BY ' + partition_col if partition_col else ''}
                ORDER BY date_trunc('month', date)
            )) / NULLIF(LAG(AVG("{price_col}")) OVER (
                {'PARTITION BY ' + partition_col if partition_col else ''}
                ORDER BY date_trunc('month', date)
            ), 0) * 100, 2
        ) AS var_percent
    FROM "{SCHEMA}"."{product}"
    WHERE date >= :date_from AND date <= :date_to
    GROUP BY {partition_col or '1'}, date_trunc('month', date)
    ORDER BY month;
    """
    with get_engine().connect() as conn:
        df_var = pd.read_sql(text(q), conn, params={"date_from": date_from, "date_to": date_to})
    st.dataframe(df_var)
    fig_var = px.bar(df_var, x="month", y="var_percent", title="Variação mensal (%)", color="var_percent",
                     color_continuous_scale="RdBu")
    st.plotly_chart(fig_var, use_container_width=True)
except Exception as e:
    st.warning(f"Erro ao calcular variação: {e}")

# --- Dados brutos ---
st.subheader("📋 Amostra de dados")
st.dataframe(df.tail(200), use_container_width=True)

st.markdown("---")
st.caption("💡 Compatível com SQLAlchemy 2.0+ — desenvolvido para análise exploratória de dados de commodities.")
