def verificar_par_impar(numero):
    if numero % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

numero_matricula = int(input("Digite o número da matrícula: "))
verificar_par_impar(numero_matricula)