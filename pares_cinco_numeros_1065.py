#Desafio número 1065: "Pares entre Cinco Números"

#Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e 
# mostre esta informação.
#Entrada
#O arquivo de entrada contém 5 valores inteiros quaisquer.
#Saída
#Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())

valores_pares = 0

if valor_1 % 2 == 0:
    valores_pares = valores_pares + 1
else:
    valores_pares = 0

if valor_2 % 2 == 0:
    valores_pares = valores_pares + 1
else:
    valores_pares = 0

if valor_3 % 2 == 0:
    valores_pares = valores_pares + 1
else:
    valores_pares = 0

if valor_4 % 2 == 0:
    valores_pares = valores_pares + 1
else:
    valores_pares = 0


if valor_5 % 2 == 0:
    valores_pares = valores_pares + 1
else:
    valores_pares = 0



print("{} valores pares".format(valores_pares))
