#Automação de processos
# !pip install pa
import pyautogui as pa
import pyperclip # conserta problema de caracteresvictorssantos572@gmail.com        
import time 

# pa.click ->clicar
# pa.write ->escrever
# pa.press ->pressionar
# pa.hotkey ->atalho

pa.PAUSE = 1 #delay para ajudar o processamento
pa.FAILSAFE = True #colocar o mouse no canto superior para cancelar a operação

# Passo 1: Entrar no sistema da empresa (link do drive)
pa.hotkey('win')
pa.write("chrome")
pa.press("enter")
pa.hotkey("ctrl","t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pa.hotkey("ctrl","v")
# problema de velocidade, logo usar o pause
pa.press("enter")
time.sleep(3)

# Passo 2: Navegar até o relatório (Pasta Exportar)
pa.click(x=332, y=372,clicks=2)
time.sleep(2)

# Passo 3: Exportar o relatório (Download)
pa.click(x=332, y=372,clicks=1) #button="right"
pa.click(x=806, y=182,clicks=1)
pa.click(x=577, y=587,clicks=1)
time.sleep(3)

# Passo 4: Calcular os indicadores (faturamento e quantidade de produtos)
import pandas #pacote excel, trabalhar com planilhas

tabela = pandas.read_excel(r"C:\Users\victo\Downloads\Vendas - Dez.xlsx") # r = raw, ou seja, sem caracter especial
#display(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# Passo 5: Enviar um email para a diretoria

#abrir aba e entrar no gmail
pa.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pa.hotkey("ctrl","v")
pa.press("enter")
#clicar no botao escrever
time.sleep(2)
pa.click(x=125, y=184)
time.sleep(1)
#informações do email
#destinatário
pa.write("victorssantos572@gmail.com")
pa.press("tab")

#assunto
pa.press("tab")
pyperclip.copy("Relatório de vendas")
pa.hotkey("ctrl","v")
pa.press("tab") #pula para o próximo campo
#Corpo
texto = f"""Prezada diretoria, bom dia

o faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de:{quantidade:,}
    
Abs
Victor"""

pyperclip.copy(texto)
pa.hotkey("ctrl","v")
#enviar
pa.hotkey("ctrl","enter")