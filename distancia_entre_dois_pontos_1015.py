#Desafio número 1015: "Distância Entre Dois Pontos"

import math

x_1_str, y_1_str = input().split(" ")
x_2_str, y_2_str = input().split(" ")

x_1 = float(x_1_str)
y_1 = float(y_1_str)
x_2 = float(x_2_str)
y_2 = float(y_2_str)

def formula_da_distancia_entre_dois_pontos ():
    formula = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    print("{:.4f}".format(formula))

formula_da_distancia_entre_dois_pontos()



