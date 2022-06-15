#Desafio número 1043: "Triângulo"

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

perimetro = A + B + C
area_trapezio = (A + B) * C/2

def pode_ser_triangulo ():
    if (abs(B - C) < A < B + C) and (abs(A - C) < B < A + C) and abs(A - B) < C < A + B:
        print("Perimetro = {}".format(perimetro))
    else:
        print("Area = {}".format(area_trapezio))

pode_ser_triangulo()

