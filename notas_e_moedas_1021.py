#Desafio de número 1021: Notas e Moedas
# Wrong answer (0%)

valor_inserido = float(input())

print("NOTAS:")

num_notas_100 = valor_inserido//100 
print("{:.0f} nota(s) de R$ 100.00".format(num_notas_100))

valor_residual = valor_inserido - (100 * num_notas_100)
num_notas_50 = valor_residual//50
print("{:.0f} nota(s) de R$ 50.00".format(num_notas_50))

valor_residual = valor_residual - (50 * num_notas_50)
num_notas_20 = valor_residual//20
print("{:.0f} nota(s) de R$ 20.00".format(num_notas_20))

valor_residual = valor_residual - (20 * num_notas_20)
num_notas_10 = valor_residual//10
print("{:.0f} nota(s) de R$ 10.00".format(num_notas_10))

valor_residual = valor_residual - (10 * num_notas_10)
num_notas_5 = valor_residual//5
print("{:.0f} nota(s) de R$ 5.00".format(num_notas_5))

valor_residual = valor_residual - (5 * num_notas_5)
num_notas_2 = valor_residual//2
print("{:.0f} nota(s) de R$ 2.00". format(num_notas_2))

print("MOEDAS:")

valor_residual = valor_residual - (2 * num_notas_2)
num_moedas_1 = valor_residual//1
print("{:.0f} moeda(s) de R$ 1.00".format(num_moedas_1))

valor_residual = valor_residual - (1 * num_moedas_1)
num_moedas_05 = valor_residual//0.5
print("{:.0f} moeda(s) de R$ 0.50".format(num_moedas_05))

valor_residual = valor_residual - (0.5 * num_moedas_05)
num_moedas_025 = valor_residual//0.25
print("{:.0f} moeda(s) de R$ 0.25".format(num_moedas_025))

valor_residual = valor_residual - (0.25 * num_moedas_025)
num_moedas_010 = valor_residual//0.10
print("{:.0f} moeda(s) de R$ 0.10".format(num_moedas_010))

valor_residual = valor_residual - (0.1 * num_moedas_010)
num_moedas_005 = valor_residual//0.05
print("{:.0f} moeda(s) de R$ 0.05".format(num_moedas_005))

valor_residual = valor_residual - (0.05 * num_moedas_005)
num_moedas_001 = valor_residual//0.01
print("{:.0f} moeda(s) de R$ 0.01".format(num_moedas_001))