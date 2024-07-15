from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = Firefox()

url = 'https://google.com'
browser.get(url)

input_area = browser.find_element(By.NAME, "q")
input_area.send_keys('Instituto Joga Junto')
input_area.send_keys(Keys.ENTER)

time.sleep(5) 

result_search = browser.find_elements(By.TAG_NAME, 'h3')

for result in result_search:
    if 'Instituto Joga Junto' in result.text:
        result.click()
    break

title = browser.title
assert 'Instituto Joga Junto' in title, "Página incorreta na busca"

def Formulario(nome,email,assunto,mensagem):
    input_nome = browser.find_element(By.ID, "nome")
    input_nome.send_keys(nome)

    input_email = browser.find_element(By.ID, "email")
    input_email.send_keys(email)

    input_assunto = browser.find_element(By.ID, "assunto")
    select = Select(input_assunto)
    select.select_by_visible_text(assunto)

    input_msg = browser.find_element(By.ID, "mensagem")
    input_msg.send_keys(mensagem)

Formulario("Daniel de Araujo Santana","daniel.xdkk@gmal.com","Ser facilitador","Funções foram adicionadas no codigo - Hermes Quality")

button_enviar = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")
button_enviar.click()

time.sleep(10)

browser.quit()