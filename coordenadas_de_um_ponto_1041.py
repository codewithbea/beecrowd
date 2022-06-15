#Desafio número 1041: "Coordenadas de um Ponto"

x, y = input().split()

x = float(x)
y = float(y)

#Quadrante 1
if x > 0 and y > 0:
    print("Q1")
#Quadrante 2
if x < 0 and y > 0:
    print("Q2")
#Quadrante 3
if x < 0 and y < 0:
    print("Q3")
#Quadrante 4
if x > 0 and y < 0:
    print("Q4")
#Origem
if x == 0 and y == 0:
    print("Origem")
#Eixo X
if x == 0:
    print("Eixo Y")
#Eixo Y
if y == 0:
    print("Eixo X")


