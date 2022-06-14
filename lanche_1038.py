#Desafio número 1038: "Lanche"

código_lanche, quant_lanche = input().split()

código_lanche = int(código_lanche)
quant_lanche = int(quant_lanche)

lista_lanches = [4.00, 4.50, 5.00, 2.00, 1.50]
preco_final = lista_lanches[código_lanche - 1] * quant_lanche

print("Total: R$ {:.2f}".format(preco_final))
