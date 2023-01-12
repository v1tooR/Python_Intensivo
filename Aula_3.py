from selenium import webdriver
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Chrome()

# Passo 1: Pegar a cotação do dolar

#entrar no google
navegador.get("https://www.google.com/")

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")#xpath = seleciona elemento dentro da pagina web

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath',
                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Passo 2: Pegar a cotação do euro
navegador.get("https://www.google.com/")

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")#xpath = seleciona elemento dentro da pagina web

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath',
                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


# Passo 3: Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_dolar, cotacao_euro, cotacao_ouro)
#navegador.quit()

# Passo 4: Importar a base de dados e atualizar a base
import pandas as pd
import openpyxl as px

tabela = pd.read_excel("Aula 3/Produtos.xlsx")
#display(tabela)

# Passo 5: Recalcular os preços

#atualizar a cotação
tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)#linha e coluna
tabela.loc[tabela["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)#linha e coluna
tabela.loc[tabela["Moeda"] == "Ouro","Cotação"] = float(cotacao_ouro)#linha e coluna

#preço de compra = cotação * preço original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
#preço de venda = preço de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
#display(tabela)

# Passo 6: Exportar a base atualizada
tabela.to_excel("Produtos Atualizado.xlsx", index=False)