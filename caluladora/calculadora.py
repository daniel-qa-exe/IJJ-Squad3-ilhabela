"""
logica funcional 

input operador
input numero 1 
input numero 2

match case pra fazer a comparação desse input 

cases com a operação
    o calculo com o retorno

"""
print("Calculadora simples, calcule soma ,subtração, multiplicação ou divisão")
operador = input("Escolha uma operação (+, -, *, /): ")
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

match operador:
    case  "+":
        soma = numero1 + numero2
        print(f"O resultado do seu calculo é {soma}")
    case "-":
        subt = numero1 - numero2
        print(f"O resultado do seu calculo é {subt}")
    case "*":
        mult = numero1 * numero2
        print(f"O resultado do seu calculo é {mult}")
    case "/":
        div = numero1 / numero2
        print(f"O resultado do seu calculo é {div}")