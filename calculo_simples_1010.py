#Desafio 'Cálculo Simples' - 1010

peças_1, numero_de_peças_1, valor_unitario_peça_1 = input().split(" ")
peças_2, numero_de_peças_2, valor_unitario_peça_2 = input().split(" ")

total_01 = int(numero_de_peças_1) * float(valor_unitario_peça_1)
total_02 = int(numero_de_peças_2) * float(valor_unitario_peça_2)

total_a_pagar = total_01 + total_02

print('VALOR A PAGAR: R$ {:.2f}'.format(total_a_pagar))
