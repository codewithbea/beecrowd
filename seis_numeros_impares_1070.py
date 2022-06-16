

numero = int(input())
i = 0
if numero % 2 == 0:
    numero = numero + 1
else:
    numero = numero + 0

while i < 6:
    print(numero)
    i = i + 1
    numero = numero + 2
