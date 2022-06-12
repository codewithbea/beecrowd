# Desafio 1008 do beecrowd

numero_funcionario = int(input())
numero_horas_str = input()
valor_hora_str = input()

salario = (int(float(numero_horas_str)) * float(valor_hora_str))

print("NUMBER =", numero_funcionario)
print("SALARY = U$ {:.2f}".format(salario))
