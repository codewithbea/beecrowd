# Desafio número 1018: "Cédulas"

valor_inserido = int(input())
print(valor_inserido)


num_notas_100 = valor_inserido//100 
print("{} nota(s) de R$ 100,00".format(num_notas_100))

valor_residual = valor_inserido - (100 * num_notas_100)
num_notas_50 = valor_residual//50
print("{} nota(s) de R$ 50,00".format(num_notas_50))

valor_residual = valor_residual - (50 * num_notas_50)
num_notas_20 = valor_residual//20
print("{} nota(s) de R$ 20,00".format(num_notas_20))

valor_residual = valor_residual - (20 * num_notas_20)
num_notas_10 = valor_residual//10
print("{} nota(s) de R$ 10,00".format(num_notas_10))

valor_residual = valor_residual - (10 * num_notas_10)
num_notas_5 = valor_residual//5
print("{} nota(s) de R$ 5,00".format(num_notas_5))

valor_residual = valor_residual - (5 * num_notas_5)
num_notas_2 = valor_residual//2
print("{} nota(s) de R$ 2,00". format(num_notas_2))

valor_residual = valor_residual - (2 * num_notas_2)
num_notas_1 = valor_residual//1
print("{} nota(s) de R$ 1,00".format(num_notas_1))