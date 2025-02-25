import pandas as pd  

# Criando os dados fictícios
dados = {
    "ID": [1, 2, 3, 4, 5],
    "Nome do Projeto": ["Parque Eólico Norte", "Usina Solar Bahia", "Parque Eólico Sul", "Usina Solar Nordeste", "Expansão Rede Norte"],
    "Tipo": ["Eólico", "Solar", "Eólico", "Solar", "Distribuição"],
    "Início": ["2024-01-01", "2024-02-15", "2024-03-10", "2023-01-05", "2024-07-01"],
    "Término": ["2024-06-30", "2024-09-30", "2024-12-20", "2024-06-30", "2025-06-30"],
    "Status": ["Em Andamento", "Em Andamento", "Atrasado", "Concluído", "Não Iniciado"],
    "Orçamento Planejado (R$)": [100000000, 150000000, 200000000, 180000000, 250000000],
    "Orçamento Gasto (R$)": [50000000, 80000000, 150000000, 180000000, 0],
    "% Concluído": [50, 40, 70, 100, 0],
    "Atraso (dias)": [0, 10, 45, 15, 0],
    "Eficiência Operacional (%)": [92, 88, 85, 95, None]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Convertendo datas para formato correto
df["Início"] = pd.to_datetime(df["Início"])
df["Término"] = pd.to_datetime(df["Término"])

# Salvando em um arquivo Excel
df.to_excel("projetos.xlsx", index=False)

print("Arquivo 'projetos.xlsx' criado com sucesso!")
