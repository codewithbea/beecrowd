
valor_inserido = int(input())
lista_notas = [100,50,20,10,5,2,1]

print(valor_inserido)

def new_func(lista_notas, n):
    valor_nota = lista_notas[n]
    return valor_nota

for n in range (0,7):
    valor_nota = new_func(lista_notas, n)
    num_de_notas = valor_inserido//valor_nota
    print("{} nota(s) de R$ {},00".format(num_de_notas, valor_nota))
    valor_inserido = valor_inserido - (valor_nota * num_de_notas)