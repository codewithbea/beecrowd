#Desafio Salário com Bônus - 1009

nome_funcionario = input()
salario_fixo_str = input()
vendas_realizadas_str = input()

salario_bônus = float(salario_fixo_str) + (float(vendas_realizadas_str) * 0.15)

print("TOTAL = R$ {:.2f}".format(salario_bônus))