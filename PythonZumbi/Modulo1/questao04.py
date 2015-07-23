#!/usr/bin/python
preco = input("Digite o preco do produto: ")
porcentagem = input("Digite o desconto: ")


resultado = porcentagem / 100.0 * preco

print "O valor do desconto e:",resultado
print "Valor a pagar:",preco - resultado