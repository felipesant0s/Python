#!/usr/bin/python

distancia = float(input("Digite a distancia da viagem: "))
velocidade = float(input("Digite a velocidade media: "))
tempo = distancia/velocidade
min = (round(tempo % 1, 2))
min = (min * 60)

print('O tempo esperado da viagem e de {:.0f} horas e {:.0f} minutos'.format(tempo,min))