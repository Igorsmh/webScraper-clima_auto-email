from selenium.webdriver.common.by import By
from time import sleep
from src import init_driver




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

# temperatura
amanha_temp = driver.find_elements(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span/span")
dep_amanha_temp = driver.find_elements(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span/span")
dep_dep_amanha_temp = driver.find_elements(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span/span")

a_t = amanha_temp[3].text
d_a_t = dep_amanha_temp[3].text
d_d_a_t = dep_dep_amanha_temp[3].text

# Condição do clima
amanha_cond = driver.find_elements(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span/img")
dep_amanha_cond = driver.find_elements(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span/img")
dep_dep_amanha_cond = driver.find_elements(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span/img")

a_c = amanha_cond[0].get_attribute('alt')
d_a_c = dep_amanha_cond[0].get_attribute('alt')
d_d_a_c = dep_dep_amanha_cond[0].get_attribute('alt')

print(f"Amanha: {a_t} {a_c}  \n Depois de amanha:  {d_a_t} {d_a_c}  \n Depois de depois de amanha: {d_d_a_t} {d_d_a_c} " )

input('')
driver.close()