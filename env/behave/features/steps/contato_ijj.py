#baixar extensão cucumber
#pip install behave
#update commit

from behave import given, when, then 
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@given(u'estou na pagina  do instituto joga junto')
def step_on_instituto_page(context):
    context.browser = Firefox()
    context.browser.get("https://www.jogajuntoinstituto.org/")
    browser_title = context.browser.title
    assert "Instituto Joga Junto" in browser_title, "tiulo não encontrado"

@when(u'preencho o formulario')
def step_fill_form(context):
    context.browser.find_element(By.ID, "nome").send_keys("Daniel de Araújo Santana")
    context.browser.find_element(By.ID, "email").send_keys("daniel.xdkk@gmail.com")
    context.browser.find_element(By.ID, "body").send_keys("minha primeira automação com behave")
    select_subjects = context.browser.find_element(By.ID, "assunto")
    select = Select(select_subjects)
    select.select_by_visible_text()
    
@when(u'aperto o botao de enviar')
def step_submit():
    pass
@then(u'os dados sao recebidos com sucesso')
def step_confirmation():
    pass
