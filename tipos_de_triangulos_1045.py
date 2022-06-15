#Desafio número 1045: "Tipos de triangulos"

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

list_num = [A, B, C]
list_num.sort()

A = list_num[2]
B = list_num[1]
C = list_num[0]

existencia_triangulo = A >= B + C 
pitagoras = A**2 == B**2 + C**2
triangulo_obtusangulo = A**2 > B**2 + C**2
triangulo_acutangulo = A**2 < B**2 + C**2
triangulo_equilatero = A == B == C
triangulo_isosceles = A == B != C or B == C != A or C == A != B


if existencia_triangulo == True:
    print("NAO FORMA TRIANGULO")

if existencia_triangulo == False and pitagoras:
    print("TRIANGULO RETANGULO")
if existencia_triangulo == False and triangulo_obtusangulo:
    print("TRIANGULO OBTUSANGULO")
if existencia_triangulo == False and triangulo_acutangulo:
    print("TRIANGULO ACUTANGULO")
if existencia_triangulo == False and triangulo_equilatero:
    print("TRIANGULO EQUILATERO")
if existencia_triangulo == False and triangulo_isosceles:
    print("TRIANGULO ISOSCELES")
