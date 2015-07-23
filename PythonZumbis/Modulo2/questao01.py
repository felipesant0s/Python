#!/usr/bin/python
a = int(input('Valor do Lado 1 : '))
b = int(input('Valor do Lado 2 : '))
c = int(input('Valor do Lado 3 : '))
ok = False

if ((a + b) > c) == True and ((b + c) > a) == True and ((a + c) > b) == True:
    print('Triangulo Existe')
    ok = True
else:
    print('Não existe')
if ok:
    if (a == b) and (a == c) and (b == c):
        print('Triagulo Equilatero')
    elif (a == b) or (a == c) or (b == c):
        print('Triagulo Isosceles')
    elif (a != b) and (a != c) and (b != c):
        print('Triangulo Escaleno')
    else:
        print('Erro de Lógica')
else:
    print('Não é possivel calcular triangulo inexistente')