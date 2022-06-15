#Desafio número 1046: "Tempo de Jogo"

x, y = input().split()

x = int(x)
y = int(y)

if x == y:
    print("O JOGO DUROU 24 HORA(S)")
if x > y and x != y:
    x = x - 12
    y = y + 12
    print("O JOGO DUROU {} HORA(S)".format(y - x))
elif y > x and x != y:
    print("O JOGO DUROU {} HORA(S)".format(abs(x - y)))


