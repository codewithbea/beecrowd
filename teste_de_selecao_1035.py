# Desafio 1035: "Teste de Seleção 1"

A_str, B_str, C_str, D_str = (input().split(" "))

A = int(A_str)
B = int(B_str)
C = int(C_str)
D = int(D_str)

def formula():
    if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A%2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")

formula()