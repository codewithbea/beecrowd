


salario = float(input())

if salario > 0 and salario <= 400.00:
    reajuste = salario * 0.15
    salario = salario + reajuste
    porcentagem = 15
elif salario > 400.00 and salario <= 800.00:
    reajuste = salario * 0.12
    salario = salario + reajuste
    porcentagem = 12
elif salario > 800.00 and salario <= 1200.00:
    reajuste = salario * 0.10
    salario = salario + reajuste
    porcentagem = 10
elif salario > 1200.00 and salario <= 2000.00:
    reajuste = salario * 0.07
    salario = salario + reajuste
    porcentagem = 7
elif salario > 2000.00:
    reajuste = salario * 0.04
    salario = salario + reajuste
    porcentagem = 4

print("Novo salario: {:.2f}".format(salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(porcentagem))

