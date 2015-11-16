#!/usr/bin/env python

import socket
import struct
import time
  
# Dados para a comunicacao Modbus TCP
TCP_IP = 'localhost'
TCP_PORT = 50001
BUFFER_SIZE = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
  
try:
   # Entrada das informacoes MODBUS
   print("\nDIGITE AS INFORMACOES\n")
   endUTR = input("Endereco da UTR : ")
   funcaoModbus = input("Escolha uma Funcao Modbus: \n(1) Read Coils (2) Read Input Discretes (3) Read Holding Registers (4) Read Input Registers: ")
   inicioRegistradores = input("Inicio dos Registradores : ")
   numRegistradores = input("Numero de registradores : ")
  
   # Criando solicitacao pacote
   req = struct.pack('>3H 2B 2H', 0, 0, 6, int(endUTR), int(funcaoModbus), int(inicioRegistradores), int(numRegistradores))
   sock.send(req)

   BUFFER_SIZE = (3*2) + (3*1) + (int(numRegistradores)*2)
   rec = sock.recv(BUFFER_SIZE)

   def setB():
       global BH
       BH = 'B' #1
   def setH():
       global BH
       BH = 'H' #2

   functionLookup = {
       1 : setB,
       2 : setB,
       3 : setH,
       4 : setH
   }
   functionLookup[int(funcaoModbus)]()

   s = struct.Struct('>3H 3B %s%s' %(numRegistradores, BH))
   data = s.unpack(rec)

   # Mostra os valores dos registradores
   print("\nREGISTRADORES\n")
   for i in range(6, 6+int(numRegistradores)):
       registradorAtual = str((i - 6) + int(inicioRegistradores)).zfill(2)
       print(" Endereco #%s : %s" %(registradorAtual, data[i]))

   time.sleep(2);
  
finally:
   print('\n :* \n')
   sock.close()
