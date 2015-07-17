#!/usr/bin/python
import mysql.connector
import csv

db = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="root", database="teste")
cursor = db.cursor()
insert_data = "REPLACE INTO digitais (pto, id, descricao, estado) VALUES (%s, %s, %s, %s)"

with open('/media/CODIGOS/Python/PythonMySQL/sage.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for data in csv_reader:
        cursor.execute(insert_data, data)
        db.commit()

cursor.close()
db.close()
