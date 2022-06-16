

valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())
valor_6 = float(input())

valores_positivos = 0


if valor_1 > 0:
    valores_positivos = valores_positivos + 1
if valor_2 > 0:
    valores_positivos = valores_positivos + 1
if valor_3 > 0:
    valores_positivos = valores_positivos + 1
if valor_4 > 0:
    valores_positivos = valores_positivos + 1
if valor_5 > 0:
    valores_positivos = valores_positivos + 1
if valor_6 > 0:
    valores_positivos = valores_positivos + 1

print("{} valores positivos".format(valores_positivos))