# Desafio número 1013: "O Maior"

import math

primeiro_val_str, segundo_val_str, terceiro_val_str = input().split(" ")

A = int(primeiro_val_str)
B = int(segundo_val_str)
C = int(terceiro_val_str)

def formula_maior_valor():
    maior_AB = (A + B + abs(A - B))/2
    resultado_final = (maior_AB + C + abs(maior_AB - C))/2
    print("{:.0f} eh o maior".format(resultado_final))

formula_maior_valor()


