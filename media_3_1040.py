#Desafio número 1040: "Média 3"

N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)


formula_media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1)/10
print("Media: {:.1f}".format(formula_media))

if formula_media >= 7.0:
    print("Aluno aprovado.")
elif formula_media < 5:
    print("Aluno reprovado.")
elif formula_media <= 6.9 and formula_media >= 5.0:
    print("Aluno em exame.")
    N5 = float(input())
    print("Nota do exame: {:.1f}".format(N5))
    nova_media = (N5 + formula_media)/2
    if nova_media >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(nova_media))
    elif nova_media < 5.0:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(nova_media))