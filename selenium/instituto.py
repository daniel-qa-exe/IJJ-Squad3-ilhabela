from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def inicia_navegador():
    return Firefox()

def pesquisa_google(browser, pesquisa):
    url = 'https://google.com'
    browser.get(url)
    input_area = browser.find_element(By.NAME, "q")
    input_area.send_keys(pesquisa)
    input_area.send_keys(Keys.ENTER)
    time.sleep(5)
    

def click_resultado(browser, txt_padrao):
    result_search = browser.find_elements(By.TAG_NAME, 'h3')
    for result in result_search:
        if txt_padrao in result.text:
            result.click()
        break
def assert_pagina(browser,titulo_padrao):
    title = browser.title
    assert titulo_padrao in title, "Página incorreta na busca"

def Formulario(browser, nome, email, assunto, mensagem):
    browser.find_element(By.ID, "nome").send_keys(nome)
    browser.find_element(By.ID, "email").send_keys(email)
    input_assunto = browser.find_element(By.ID, "assunto")
    select = Select(input_assunto)
    select.select_by_visible_text(assunto)
    browser.find_element(By.ID, "mensagem").send_keys(mensagem)

def submit_form(browser):
    button_enviar = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")
    button_enviar.submit()

browser = inicia_navegador()
pesquisa_google(browser, 'Instituto Joga Junto')
click_resultado(browser,'Instituto Joga Junto')
assert_pagina(browser,'Instituto Joga Junto')
Formulario(browser,"Daniel de Araujo Santana","daniel.xdkk@gmail.com","Ser facilitador","Funções foram adicionadas no codigo - Hermes Quality")
submit_form(browser)
time.sleep(7)
browser.quit()