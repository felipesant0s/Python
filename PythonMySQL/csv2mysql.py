#!/usr/bin/python
import mysql.connector
import csv
import os
import commands

os.system("ssh comissionamento 'cd $SAGE ; ./geracsv.sh'")

db = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="root", database="sage")
cursor = db.cursor()
insert_sage = "REPLACE INTO digitais (pto, id, descricao, estado, qualidade) VALUES (%s, %s, %s, %s, %s)"

with open('/media/CODIGOS/Python/PythonMySQL/sage.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for sage in csv_reader:
        cursor.execute(insert_sage, sage)
        db.commit()

cursor.close()
db.close()
