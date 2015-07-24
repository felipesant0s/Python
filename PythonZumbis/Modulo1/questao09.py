#!/usr/bin/python
dias = int(input('Digite a quentidade em dias de aluguel do carro: '))
km = float(input('Digite quantos Km foram rodados: '))

valor=(dias*60)+(km*0.15)

print('O valor a pagar e de R${:.2f} '.format(valor,dias,km))