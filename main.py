# ESTRUTURA DO PROJETO
# Entrada → Tratamento → KPIs → Saída

# 1. Entrada → carregar base (CSV/Excel)
# 2. Tratamento → limpar dados
# 3. KPIs → calcular métricas
# 4. Saída → salvar arquivo final

import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base de dados
df = pd.read_csv("dados_cartoes.csv")

# Tratamento dos dados
df["data"] = pd.to_datetime(df["data"])
df = df.dropna()  

# KPIs
total = df["valor"].sum()
qtd_transacoes = df.shape[0]
ticket_medio = df["valor"].mean()

    # Taxa de aprovação
taxa_aprovacao = (df["status"] == "Aprovado").mean() * 100

    # Gasto por categoria
gasto_categoria = df.groupby("categoria")["valor"].sum()

    # Gasto por método de pagamento
gasto_metodo = df.groupby("metodo_pagamento")["valor"].sum()

# Saída
kpis = pd.DataFrame({
    "total": [total],
    "qtde_transacoes": [qtd_transacoes],
    "ticket_medio": [ticket_medio],
    "taxa_aprovacao": [taxa_aprovacao]
})

kpis.to_csv("kpis_cartoes.csv", index=False)

print("KPIs calculados e salvos em 'kpis_cartoes.csv'")

def exibir_resultados(kpis, gasto_categoria, metodo_pagamento):
    print("\n📊 KPIs:")
    print(kpis)

    print("\n📊 Categoria:")
    print(gasto_categoria)

    gasto_categoria.plot(kind="bar")
    plt.show()