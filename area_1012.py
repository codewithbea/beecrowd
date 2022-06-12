A_str, B_str, C_str = input().split(" ")

A = float(A_str)
B = float(B_str)
C = float(C_str)
pi = 3.14159

def area_triangulo():
    area_triangulo = (A * C)/2
    print('TRIANGULO = {:.3f}'.format(area_triangulo))

def area_circulo():
    area_circulo = pi * C**2
    print('CIRCULO: {:.3f}'.format(area_circulo))

def area_trapezio():
    area_trapezio = (A + B) * C/2
    print('TRAPEZIO: {:.3F}'.format(area_trapezio))

def area_quadrado():
    area_quadrado = B**2
    print('QUADRADO: {:.3F}'.format(area_quadrado))

def area_retangulo():
    area_retangulo = A * B
    print('RETANGULO: {:.3F}'.format(area_retangulo))

area_triangulo()
area_circulo()
area_trapezio()
area_quadrado()
area_retangulo()
