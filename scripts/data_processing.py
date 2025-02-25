import pandas as pd

def load_data():
    """Carrega os dados do Excel e faz o pré-processamento necessário."""
    df = pd.read_excel("data/projetos.xlsx")

    # Convertendo colunas de data
    df["Início"] = pd.to_datetime(df["Início"])
    df["Término"] = pd.to_datetime(df["Término"])

    # Criando uma coluna de orçamento estourado
    df["Orçamento Estourado"] = df["Orçamento Gasto (R$)"] > df["Orçamento Planejado (R$)"]

    # Criando uma métrica de atraso ajustada
    df["Atraso Corrigido"] = df.apply(lambda row: 0 if row["Status"] == "Concluído" else row["Atraso (dias)"], axis=1)

    return df
