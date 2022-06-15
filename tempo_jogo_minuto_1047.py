#Desafio 1047 - "Tempos de jogo com Minutos"
# 100% Wrong Anwser

hora_i, minuto_i, hora_f, minuto_f = input().split()

hora_i = int(hora_i) 
minuto_i = int(minuto_i) 
hora_f = int(hora_f) 
minuto_f= int(minuto_f) 

total_h = hora_f - hora_i
total_m = minuto_f - minuto_i

if(total_h < 0):
    total_h = 24 + (hora_f - hora_i)

if(total_m < 0):
    total_m = 60 + (minuto_f - minuto_i)
    total_h = total_h - 1

if(hora_f == hora_i and minuto_f == minuto_i):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTOS")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(total_h, total_m))
