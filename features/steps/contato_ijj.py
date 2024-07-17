from behave import given, when, then
from selenium.webdriver import Firefox


@given(u'que estou na pagina  do instituto joga junto')
def step_on_instituto(context):
    context.browser = Firefox()
    context.browser.get("https://www.jogajuntoinstituto.org/")
    browser_title = context.browser.title
    assert "Instituto Joga Junto" in browser_title, "tiulo não encontrado"

@when(u'preencho o formulario')
def step_impl(context):
   pass


@when(u'aperto o botao de enviar')
def step_impl(context):
    pass


@then(u'os dados sao recebidos com sucesso')
def step_impl(context):
    pass