import pyautogui
import pyperclip
import webbrowser
import time

from alpha_vantage.timeseries import TimeSeries

# Sua chave de API
api_key = 'NDPYMVEA4RLSRD17'

# Inicialize a classe TimeSeries com sua chave de API
ts = TimeSeries(key=api_key, output_format='pandas')

# Obtenha dados diários para uma ação específica (por exemplo, Microsoft - MSFT)
ticket = input("Digite a ação desejada: ") # 'MSFT'
data, meta_data = ts.get_daily(symbol=str(ticket), outputsize='full')

# Exiba os primeiros dados
print(data.head())

# Calcule a cotação máxima
max_price = data['2. high'].max()
min_price = data['2. high'].min()
mean_price = data['2. high'].mean()

#print(f'A cotação máxima da ação MSFT é: {max_price}')
#print(f'A cotação minima da ação MSFT é: {min_price}')
#print(f'A cotação média da ação MSFT é: {mean_price}')

max_price_formatted = round(max_price, 2)
min_price_formatted = round(min_price, 2)
mean_price_formatted = round(mean_price, 2)

print(f"""
      Ação {ticket}, cotação de fechamento:
      Máxima: {max_price_formatted}
      Minima: {min_price_formatted}
      Média: {mean_price_formatted}
      """)


destinatario = input("Destinatário: ")
assunto = "teste"
mensagem = f"""
  Prezado gestor,

  Seguem as análises solicitadas da ação

  Acção {ticket}
  Cotação máxima: R$ {max_price_formatted}
  Cotação mínima: R$ {min_price_formatted}
  Cotação média: R$ {mean_price_formatted}

Qualquer dúvida, estou à disposição!

Atte
"""
# abrir o navegador e ir para gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

pyautogui.PAUSE = 3

#clicar no botão escrever
pyautogui.click(x=193, y=233)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyautogui.click(x=1205, y=985)
