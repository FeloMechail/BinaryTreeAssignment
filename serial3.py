
from serial import *
import time
import json


ser = Serial('COM5',9600)

if(ser.isOpen() == False):
    ser.open()

print("started")


while True:
  b = ser.readline()
  time.sleep(2)
  string_n = b.decode()
  string = string_n.rstrip() 
  splitt = string.split(" ")
  temp = splitt[2]
  hum = splitt[5]
  mint = splitt[9]
  basil = splitt[11]
  mints = splitt[15]
  ros = splitt[17]
  pars = splitt[19]

  print(f'TEMPERATURE: {temp}C HUMIDITY: {hum}% MINT: {mint} BASIL: {basil} MINT S: {mints} ROSEMARY: {ros} PARSLEY: {pars}')
  with open(r'C:\Users\felop\OneDrive\Documents\web\static\read.json', "r") as json_file: 
     data = json.load(json_file) 
     data['humidity'] = hum      
     data['temperature'] = temp
     data['mint'] = mint
     data['basil'] = basil
     data['mints'] = mints
     data['ros'] = ros
     data['pars'] = pars
  with open(r'C:\Users\felop\OneDrive\Documents\web\static\read.json', "w") as json_file:
     json.dump(data, json_file)

