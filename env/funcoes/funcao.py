def saudacao(nome):
    print(f'Olá, {nome} tudo bom?')

def soma(a , b):
    resultado = a + b

    return resultado

resultado_soma = soma(1,3)
if resultado_soma < 3:
    print("resultado é menor que 3")    
else:
    print("resultado é maior que 3")


saudacao('Daniel')