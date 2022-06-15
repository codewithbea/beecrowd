#Desafio número 1044: "Multiplos"

#Leia dois valores inteiros (A e B)
A, B = input().split()
A = int(A)
B = int(B)

if A%B != 0 and B%A != 0:
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")
