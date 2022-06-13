#Desafio de número 1017: "Gasto de Combustível"

tempo_gasto_str = input()
vel_media_str = input()

tempo_gasto = int(tempo_gasto_str)
velocidade_media = int(vel_media_str)

def gasto_combustivel():
    formula = (velocidade_media * tempo_gasto)/12
    print("{:.3f}".format(formula))

gasto_combustivel()
