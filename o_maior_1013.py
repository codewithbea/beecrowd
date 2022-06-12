# Desafio número 1013: "O Maior"

primeiro_val_str, segundo_val_str, terceiro_val_str = input().split(" ")

p_val = int(primeiro_val_str)
s_val = int(segundo_val_str)
t_val = int(terceiro_val_str)

def formula_do_maior_valor():
    if(p_val > s_val and p_val > t_val):
        print('{} eh o maior'.format(p_val))
    elif(s_val > p_val and s_val > t_val):
        print('{} eh o maio'.format(s_val))
    elif(t_val > p_val and t_val > s_val):
        print('{} eh o maior'.format(t_val))

formula_do_maior_valor()


