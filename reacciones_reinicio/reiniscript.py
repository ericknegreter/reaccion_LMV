import mysql.connector
from mysql.connector import Error
import os 
import time
import subprocess, datetime
import RPi.GPIO as GPIO

#Active GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

print( "mensaje inicial antes de la espera")
time.sleep(20) # espera en segundos
print ("mensaje luego de la espera")

hosts = ('google.com', 'kernel.org', 'yahoo.com')
localhost = ('10.0.5.246')

def ping(host):
    ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w'))
    return ret == 0

def net_is_up():
    print ("[%s] Checking if network is up..." % str(datetime.datetime.now()))
    
    xstatus = 0
    if ping(localhost):
        print ("[%s] Network is up!" % str(datetime.datetime.now()))
        xstatus = 1
        
    if not xstatus:
        time.sleep(10)
        print ("[%s] Network is down :(" % str(datetime.datetime.now()))
        time.sleep(25)
        
    return xstatus

while True:
    try:
        if(net_is_up()):
            mydb = mysql.connector.connect(host="10.0.5.246", user="LMV_ADMIN", passwd="MINIMOT4", database="LMV")
            mycursor = mydb.cursor()
            sql = "SELECT estado FROM e_reaccion WHERE dispositivo = 'luz'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print(mycursor.rowcount, "record selected")
            for row in records:
                estado = int(row[0])
            mydb.close()
            if estado == 1:
                GPIO.output(18, False)
            elif estado == 0:
                GPIO.output(18, True)
            break
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
