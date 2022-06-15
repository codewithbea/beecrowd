#Desafio número 1051: "Imposto de Renda"

#0 a 2000,00 - isento
#2000.01 até 3000.00 - 8%
#3000.01 até 4500.00 - 18%
#acima de 4500.00 - 28%

salario = float(input())

if salario <= 2000.00:
    print("Isento")

if salario > 4500:
    salario_imp = salario - 4500.00
    imposto_28 = salario_imp * 0.28
    salario_imp_2 = salario - salario_imp - 3000
    imposto_18 = salario_imp_2 * 0.18
    salario_imp_3 = salario - salario_imp - salario_imp_2 - 2000
    imposto_8 = salario_imp_3 * 0.08
    print("R$ {:.2f}".format(imposto_8 + imposto_18 + imposto_28))

if salario > 3000.01 and salario <= 4500.00:
    salario_imp_2 = salario - 3000
    imposto_18 = salario_imp_2 * 0.18
    salario_imp_3 = salario - salario_imp_2 - 2000
    imposto_8 = salario_imp_3 * 0.08
    print("R$ {:.2f}".format(imposto_8 + imposto_18))

if salario > 2000 and salario <= 3000:
    salario_imp_3 = salario - 2000
    imposto_8 = salario_imp_3 * 0.08
    print("R$ {:.2f}".format(imposto_8))
