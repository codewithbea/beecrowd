#Desafio número 1042: "Sort Simples"

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

lista_num = [a, b, c]
lista_num.sort()

print(lista_num[0], lista_num[1], lista_num[2], sep='\n', end='\n\n')

print(a, b, c, sep='\n')