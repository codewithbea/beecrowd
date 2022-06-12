# Desafio 1014: "Consumo"
# Calculo do consumo médio de um automóvel com 3 casas decimais. 

distancia_total_str = input()
combustivel_total_str = input()

distancia_total = int(distancia_total_str)
combustivel_total = float(combustivel_total_str)

def consumo_medio():
    consumo_medio = distancia_total / combustivel_total
    print('{:.3f} km/l'.format(consumo_medio))

consumo_medio()
