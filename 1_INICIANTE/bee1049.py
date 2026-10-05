coluna_vertebral = input()
tipo = input()
alimentacao = input()

if coluna_vertebral == "vertebrado":
    if tipo == "ave":
        if alimentacao == "carnivoro":
            print("aguia")
        elif alimentacao == "onivoro":
            print("pomba")
    elif tipo == "mamifero":
        if alimentacao == "onivoro":
            print("homem")
        elif alimentacao == "herbivoro":
            print("vaca")
            
elif coluna_vertebral == "invertebrado":
    if tipo == "inseto":
        if alimentacao == "hematofago":
            print("pulga")
        elif alimentacao == "herbivoro":
            print("lagarta")
    elif tipo == "anelideo":
        if alimentacao == "hematofago":
            print("sanguessuga")
        elif alimentacao == "onivoro":
            print("minhoca")