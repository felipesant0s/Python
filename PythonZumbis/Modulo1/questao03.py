#!/usr/bin/python
dias=int(input('Digiteo valor de dias Dias: '))
horas=int(input('Digite o valor das Horas: '))
minutos=int(input('Digite o valor dos minutos minutos: '))

segundos=(minutos*60)+(horas*3600)+(dias*86400)
print "Total em segundos:",segundos
