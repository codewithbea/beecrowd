#Desafio número 1036: "Fórmula de Bhaskara"

#Leia três valores de ponto flutuante A, B e C

import math

A_str, B_str, C_str = input().split(" ")

A = float(A_str)
B = float(B_str)
C = float(C_str)

delta = (B ** 2) - 4 * A * C

if delta < 0 or delta == 0 or A == 0:
    print("Impossivel calcular")
else: 
    raiz_1 = (-B + math.sqrt(delta))/(2 * A)
    raiz_2 = (-B - math.sqrt(delta))/(2 * A)
    print("R1 = {:.5f}".format(raiz_1))
    print("R2 = {:.5f}".format(raiz_2))


