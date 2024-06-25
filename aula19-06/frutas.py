lista_frutas = ["maçã", "melancia", "laranja", "limão","cajá","manga"]
lista_alergias = ["abacaxi", "kiwi", "banana"]

fruta_alergica = "manga"
lista_alergias.append(fruta_alergica)

for fruta in lista_frutas:
    if fruta in lista_alergias:
        print(f"{fruta} está na lista de alergias.")