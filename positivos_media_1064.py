valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())
valor_6 = float(input())

valores_positivos = 0

if valor_1 > 0:
    valores_positivos = valores_positivos + 1
    media_1 = valor_1
else:
    media_1 = 0

if valor_2 > 0:
    valores_positivos = valores_positivos + 1
    media_2 = valor_2
else:
    media_2 = 0

if valor_3 > 0:
    valores_positivos = valores_positivos + 1
    media_3 = valor_3
else:
    media_3 = 0

if valor_4 > 0:
    valores_positivos = valores_positivos + 1
    media_4 = valor_4
else:
    media_4 = 0

if valor_5 > 0:
    valores_positivos = valores_positivos + 1
    media_5 = valor_5
else:
    media_5 = 0

if valor_6 > 0:
    valores_positivos = valores_positivos + 1
    media_6 = valor_6
else:
    media_6 = 0

media_total = (media_1 + media_2 + media_3 + media_4 + media_5 + media_6)/valores_positivos

print("{} valores positivos".format(valores_positivos))
print("{:.1f}".format(media_total))