valor = float(input("Valor da compra: "))

if valor <250.00:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")
elif valor >= 250.00 and valor < 500.00:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
elif valor >= 500.00:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%" )