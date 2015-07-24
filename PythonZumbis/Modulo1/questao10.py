#!/usr/bin/python
cigarros = int(input('Quantos Cigarros voce fuma por dia: '))
anos = int(input('Informe por quantos anos voce fuma: '))

soma = cigarros*(anos*365)
minutos = soma*10

subtrai = (minutos/60)/24

print('Voce tem %.2f dias a menos de vida' %subtrai)