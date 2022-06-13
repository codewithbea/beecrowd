#Desafio de número 1020: "Idade em Dias"

dias = int(input())

num_de_anos = dias//365 
dias_residuais = dias - (365 * num_de_anos)
print("{} ano(s)".format(num_de_anos))

num_de_meses = dias_residuais//30
dias_residuais = dias_residuais - (30 * num_de_meses)
print("{} mes(es)".format(num_de_meses))

num_de_dias = dias_residuais%30
print("{} dia(s)".format(num_de_dias))