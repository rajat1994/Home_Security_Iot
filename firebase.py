import serial
import time
import requests
import json
firebase_url = 'https://iotsecurity.firebaseio.com'
#Connect to Serial Port for communication
ser = serial.Serial('COM4', 9600, timeout=0)
#Setup a loop to send ir values at fixed intervals
#in seconds
fixed_interval = 1
while 1:
  try:
    # Readings obtained from Arduino + Infrared Sensor         
    ir_sensor = ser.readline()
    
    #current time and date
    time_hhmmss = time.strftime('%H:%M:%S')
    date_mmddyyyy = time.strftime('%d/%m/%Y')
    
    
    print ir_sensor + ',' + time_hhmmss + ',' + date_mmddyyyy 
    
    #insert record
    data = {'date':date_mmddyyyy,'time':time_hhmmss,'value': ir_sensor}
    result = requests.post(firebase_url  + '/irsensor.json', data=json.dumps(data))
    
    print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
    time.sleep(fixed_interval)
  except IOError:
    print('Error! Something went wrong.')
  time.sleep(fixed_interval)
