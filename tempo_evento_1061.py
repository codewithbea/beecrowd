#Desafio número 1061: "Tempo de um Evento"
#Wrong answer 100%

string_1, dia_inicial = input().split()
hora_inicial, minuto_inicial, segundo_inicial = input().split(" : ")

string_2, dia_final = input().split()
hora_final, minuto_final, segundo_final = input().split(" : ")

dia_inicial = int(dia_inicial)
hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
segundo_inicial = int(segundo_inicial)

dia_final = int(dia_final)
hora_final = int(hora_final)
minuto_final = int(minuto_final)
segundo_final = int(segundo_final)

total_dias = dia_final - dia_inicial
total_horas = hora_final - hora_inicial
total_minutos = minuto_final - minuto_inicial
total_segundos = segundo_final - segundo_inicial

if hora_final < hora_inicial:
    total_horas = 24 - (hora_inicial - hora_final)
    total_dias = total_dias - 1

if minuto_final < minuto_inicial:
    total_minutos = 60 - (minuto_inicial - minuto_final)
    total_horas = total_horas - 1

if segundo_final < segundo_inicial:
    total_segundos = 60 - (segundo_inicial - segundo_final)
    total_minutos = total_minutos - 1

print("{} dia(s) \n{} hora(s) \n{} minuto(s) \n{} segundo(s)".format(total_dias, total_horas, total_minutos, total_segundos))
