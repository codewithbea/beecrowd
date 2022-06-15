#Desafio número 1049: "Animal"

coluna_1 = input()
coluna_2 = input()
coluna_3 = input()

if coluna_1 == "vertebrado":
    if coluna_2 == "ave":
        if coluna_3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    elif coluna_2 == "mamifero":
        if coluna_3 == "onivoro":
            print("homem")
        else:
            print("vaca")

if coluna_1 == "invertebrado":
    if coluna_2 == "inseto":
        if coluna_3 == "hematofago":
            print("pulga")
        else: 
            print("lagarta")
    elif coluna_2 == "anelideo":
        if coluna_3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")





