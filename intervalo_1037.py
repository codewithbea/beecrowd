# Desafio número 1037: "Intervalo"

valor_inserido = float(input())

if valor_inserido < 0 or valor_inserido > 100.0:
    print("Fora de intervalo")
elif valor_inserido >= 0 and valor_inserido <= 25.0:
    print("Intervalo [0,25]")
elif valor_inserido > 25.0 and valor_inserido <= 50:
    print ("Intervalo (25,50]")
elif valor_inserido > 50.0 and valor_inserido <= 75:
    print("Intervalo (50,75]")
elif valor_inserido > 75.0 and valor_inserido <= 100.0:
    print("Intervalo (75,100]")
