idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Individuo possui idade mínima para dirigir")
elif idade == 17 and idade <= 18:
    print("Individuo tem entre 17 e 18 anos e ainda não tem idade para dirigir")
else:
    print("o individuo não possui idade mínima para dirigir")