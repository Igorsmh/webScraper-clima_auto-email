from selenium.webdriver.common.by import By
from time import sleep
import smtplib
import os
from email.message import EmailMessage
from src import init_driver

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


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

def max_min(dia):

    elementos = driver.find_elements(By.XPATH, f"//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d{dia}']/span/span")
    max_min = elementos[3].text
    return max_min

def condicao(dia):

    elementos = driver.find_elements(By.XPATH, f"//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d{dia}']/span/img")
    condicao = elementos[0].get_attribute('alt')
    return condicao


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
def enviar_email(mail):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email.send_message(mail)


enviar_email(mail)

driver.quit()