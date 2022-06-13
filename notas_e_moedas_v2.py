#Desafio 1021: "Notas e moedas"
#Continuou dando o mesmo erro: Wrong Answer (0%)



valor_inserido = float(input())
lista_notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")

def new_func(lista_notas, n):
    valor_nota = lista_notas[n]
    return valor_nota

for n in range (0,6):
    valor_nota = new_func(lista_notas, n)
    num_de_notas = valor_inserido//valor_nota
    print("{:.0f} nota(s) de R$ {:.2f}".format(num_de_notas, valor_nota))
    valor_inserido = valor_inserido - (valor_nota * num_de_notas)


lista_moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.009] #Gambiarra porque com a moeda de 1 centavo dava erro por causa das divisões // 
print("MOEDAS:")

def new_func(lista_moedas, n):
    valor_moeda = lista_moedas[n]
    return valor_moeda

for n in range (0,6):
    valor_moeda = new_func(lista_moedas, n)
    num_de_moedas = valor_inserido//valor_moeda
    print("{:.0f} moeda(s) de R$ {:.2f}".format(num_de_moedas, valor_moeda))
    valor_inserido = valor_inserido - (valor_moeda * num_de_moedas)
