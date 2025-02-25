import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.data_processing import load_data

# Carregar os dados
df = load_data()

# Configurar o layout do dashboard
st.set_page_config(page_title="Dashboard de Projetos - EnergiaTech", layout="wide")

# Título principal
st.title("📊 Dashboard de Gestão de Projetos - EnergiaTech S.A.")

# Filtros Interativos
status_selecionado = st.sidebar.selectbox("Filtrar por Status:", df["Status"].unique())
tipo_selecionado = st.sidebar.multiselect("Filtrar por Tipo:", df["Tipo"].unique(), default=df["Tipo"].unique())

# Filtrar dados
df_filtrado = df[(df["Status"] == status_selecionado) & (df["Tipo"].isin(tipo_selecionado))]

# Exibir tabela filtrada
st.write("### Projetos Selecionados")
st.dataframe(df_filtrado)

# Gráfico 1: Status dos Projetos
st.write("### Status dos Projetos")
fig1, ax1 = plt.subplots(figsize=(6,4))
sns.countplot(data=df_filtrado, x="Status", palette="viridis", ax=ax1)
ax1.set_xlabel("Status")
ax1.set_ylabel("Quantidade de Projetos")
st.pyplot(fig1)

# Gráfico 2: Orçamento Gasto vs. Planejado
st.write("### Orçamento Gasto vs. Planejado")
fig2, ax2 = plt.subplots(figsize=(8,4))
df_filtrado.plot(kind='bar', x="Nome do Projeto", y=["Orçamento Planejado (R$)", "Orçamento Gasto (R$)"], ax=ax2, color=["blue", "red"])
ax2.set_ylabel("Valor (R$)")
st.pyplot(fig2)

# Gráfico 3: Atraso Médio por Tipo de Projeto
st.write("### Atraso Médio por Tipo de Projeto")
fig3, ax3 = plt.subplots(figsize=(6,4))
df_filtrado.groupby("Tipo")["Atraso (dias)"].mean().plot(kind='bar', ax=ax3, color="orange")
ax3.set_ylabel("Média de Atraso (dias)")
st.pyplot(fig3)

st.write("📌 Esse dashboard permite acompanhar o andamento dos projetos de energia de forma dinâmica.")