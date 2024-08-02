from selenium.webdriver.common.by import By
from time import sleep
import os
from email.message import EmailMessage
from src import *

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')



driver = init_driver()
driver.get("https://www.tempo.com/rio-de-janeiro_rio-de-janeiro-l12987.htm")
sleep(3)

#Extrair a temperatura atual.
temp = driver.find_element(By.XPATH, "//span[@class='dato-temperatura changeUnitT']")
temperatura = temp.text

#Extrair a condição do tempo atual (ex. ensolarado, nublado, etc.).
cond_temp = driver.find_elements(By.XPATH,'//span[@class= "descripcion"]')
cond_temp = cond_temp[0].text

#Extrair a previsão para os próximos 3 dias (temperatura e condição do tempo)

a_t = max_min(2)
d_a_t = max_min(3)
d_d_a_t = max_min(4)


a_c = condicao(2)
d_a_c = condicao(3)
d_d_a_c = condicao(4)


#Criar o email
mail = EmailMessage()
mail['Subject'] = 'Previsão do Tempo'
mensagem = f"Previsão do Tempo para o Rio de Janeiro \n Amanha: {a_t} {a_c}\n Depois de amanha:  {d_a_t} {d_a_c} \n Depois de depois de amanha: {d_d_a_t} {d_d_a_c} "
mail['From'] = EMAIL_ADDRESS
mail['To'] = 'igorsmh@hotmail.com'
mail.add_header('Content-Type', 'text/html')
mail.set_payload(mensagem.encode('utf-8'))


#Enviar o email
enviar_email(mail)

