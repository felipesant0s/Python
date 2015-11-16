#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "localhost"
SERVER_PORT = 50001
UTR = 10


c = ModbusClient()

# Descomente para ver o TX - RX
#c.debug(True)

# Define modbus server host, porta
c.host(SERVER_HOST)
c.port(SERVER_PORT)
c.unit_id(UTR)

while True:
    # Conectando com MODBUS TCP
    if not c.is_open():
        if not c.open():
            print("Não foi possivel conectar com "+SERVER_HOST+":"+str(SERVER_PORT)+":"+str(UTR))

    #(modbus function 0x03)
    if c.is_open():
        regs = c.read_holding_registers(0,10)
        if regs:
            print("Registradores: "+str(regs))

    # sleep 2s para o próximo polling
    time.sleep(2)
