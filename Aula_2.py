#Análise de Dados

import pandas as pd #controle de dados
import plotly.express as px #criação de gráficos

#Passo 1: Importar base de dados
tabela = pd.read_csv("Aula 2/telecom_users.csv")

#Passo 2: Visualizar base de dados
# - Entender as informações
# - Descobrir erros da base

#axix -> 0 = linha; 1 = coluna

tabela = tabela.drop("Unnamed: 0", axis = 1) #axis é para localizar dentro da tabela
print(tabela)

#Passo 3: Tratamento de dados

#resolver reconhecidos de forma errada (type)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = "coerce") #passsa para numerico e conserta os erros

#resolver valores vazios

# - colunas em que tem TODOS os valores vazios
tabela = tabela.dropna(how="all" , axis = 1)
# - linhas vazias ou que possuem apenas um valor vazio
tabela = tabela.dropna(how="any" , axis = 0)

print(tabela.info()) #resume as infos da tabela

#Passo 4: Análise inicial
print(tabela["Churn"].value_counts()) #conta os valores
print(tabela["Churn"].value_counts(normalize = True).map("{:.1%}".format)) #mostra a porcentagem

#Passo 5: Análise detalhada - descobrir causas

#comparar a base de dados com a coluna Churn = desistencia de contrato

#criar grafico
#para cada coluna, criar um gráfico

#coluna = "TotalGasto"

for coluna in tabela.columns: 
    grafico = px.histogram(tabela, x = coluna, color = "Churn", text_auto = True) # comparação
    #mostrar grafico
    grafico.show()