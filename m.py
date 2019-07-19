#!/usr/bin/python3.5
import time
import sys
import mysql.connector
from datetime import date, datetime
peticion=sys.argv[1]
cnx = mysql.connector.connect(user="LMV_ADMIN", password="LABORATORIOT4", host="10.0.5.246", database="LMV")
cursor = cnx.cursor(buffered=True)
today = datetime.now()
print(today)
print("Codigo Escaneado:"+peticion)
add_proceso = ("INSERT INTO t_modulo4 (codigo_barras, fecha) VALUES ("+peticion+",'"+str(today)+"')")
data_proceso = {'codigo_barras':peticion, 'fecha':str(today)}
cursor.execute(add_proceso,)
cnx.commit()
