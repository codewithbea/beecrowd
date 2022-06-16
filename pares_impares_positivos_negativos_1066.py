

valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())
valor_4 = int(input())
valor_5 = int(input())

valores = [valor_1, valor_2, valor_3, valor_4, valor_5]
valor_par = 0
valor_impar = 0 
valor_positivo = 0
valor_negativo = 0

for n in range(0,5):
    if valores[n] % 2 == 0:
        valor_par = valor_par + 1
    elif valores[n] % 2 != 0 and valores[n] != 0:
        valor_impar = valor_impar + 1
    if valores[n] > 0:
        valor_positivo = valor_positivo + 1
    elif valores[n] < 0:
        valor_negativo = valor_negativo + 1

print("{} valor(es) par(es)".format(valor_par))
print("{} valor(es) impar(es)".format(valor_impar))
print("{} valor(es) positivo(s)".format(valor_positivo))
print("{} valor(es) negativo(s)".format(valor_negativo))