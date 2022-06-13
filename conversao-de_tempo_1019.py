# Desafio de número 1019: "Conversão de Tempo"

tempo_segundos = int(input())

num_horas = tempo_segundos//3600 
tempo_residual = tempo_segundos - (3600 * num_horas)

num_minutos = tempo_residual//60
tempo_residual = tempo_residual - (60 * num_minutos)

num_segundos = tempo_residual//1

print("{}:{}:{}".format(num_horas, num_minutos, num_segundos))
