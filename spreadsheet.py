#!/usr/bin/python
# This script is called by CRON to monitor the 
# Temperatures and Humidities in the Barrel house.
# It can also be called by watchtemps or another
# program or utility


## Use this video for help with Google API intereation
# https://www.youtube.com/watch?v=vISRn5qFrkM


## for gspread
# https://github.com/burnash/gspread

## Long Wire problems
#https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/issues/49


import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import Adafruit_DHT

# Sensor should be set to the correct
# sensor model
sensor = Adafruit_DHT.DHT22

# Using multible Raspberry Pi Pins so eerything after this is in multiples of 5
# Ceiling
pin0 = 16
# Zone 1
pin1 = 17
# Zone 2
pin2 = 18
# Zone 3
pin3 = 22
# Zone 4
pin4 = 23


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity0, temperature0 = Adafruit_DHT.read_retry(sensor, pin0)
humidity1, temperature1 = Adafruit_DHT.read_retry(sensor, pin1)
humidity2, temperature2 = Adafruit_DHT.read_retry(sensor, pin2)
humidity3, temperature3 = Adafruit_DHT.read_retry(sensor, pin3)
humidity4, temperature4 = Adafruit_DHT.read_retry(sensor, pin4)


Celsius0 = temperature0
Celsius1 = temperature1
Celsius2 = temperature2
Celsius3 = temperature3
Celsius4 = temperature4


temperature0 = 9.0/5.0 * Celsius0 + 32
temperature1 = 9.0/5.0 * Celsius1 + 32
temperature2 = 9.0/5.0 * Celsius2 + 32
temperature3 = 9.0/5.0 * Celsius3 + 32
temperature4 = 9.0/5.0 * Celsius4 + 32


humidity0 = format(humidity0, '.2f')
humidity1 = format(humidity1, '.2f')
humidity2 = format(humidity2, '.2f')
humidity3 = format(humidity3, '.2f')
humidity4 = format(humidity4, '.2f')


temperature0 = format(temperature0, '.2f')
temperature1 = format(temperature1, '.2f')
temperature2 = format(temperature2, '.2f')
temperature3 = format(temperature3, '.2f')
temperature4 = format(temperature4, '.2f')



# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
# This is not really needed except for debug
if humidity0 is not None and temperature0 is not None:
    print(temperature0)
    print(humidity0)
else:
    print('Failed to get reading on number zero. Try again!')

if humidity1 is not None and temperature1 is not None:
    print(temperature1)
    print(humidity1)
else:
    print('Failed to get reading on number one. Try again!')

if humidity2 is not None and temperature2 is not None:
    print(temperature2)
    print(humidity2)
else:
    print('Failed to get reading on number two. Try again!')

if humidity3 is not None and temperature3 is not None:
    print(temperature3)
    print(humidity3)
else:
    print('Failed to get reading on number three. Try again!')

if humidity4 is not None and temperature4 is not None:
    print(temperature4)
    print(humidity4)
else:
    print('Failed to get reading on number four. Try again!')    




# use creds to create a client to interact with the Google Drive API
## Use this video for help with Google API intereation
# https://www.youtube.com/watch?v=vISRn5qFrkM
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/etc/googleauth/client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Barrel-House-Temps").sheet1

#add a row, I think
dict = {}
dict['date'] = time.strftime('%m/%d/%Y')
dict['time'] = time.strftime('%H:%M')
dict['temperature0'] = temperature0
dict['humidity0'] = humidity0
dict['temperature1'] = temperature1
dict['humidity1'] = humidity1
dict['temperature2'] = temperature2
dict['humidity2'] = humidity2
dict['temperature3'] = temperature3
dict['humidity3'] = humidity3
dict['temperature4'] = temperature4
dict['humidity4'] = humidity4


##Debug
print dict

row = [time.strftime('%m/%d/%Y'), time.strftime('%H:%M'), temperature0, humidity0, temperature1, humidity1, temperature2, humidity2, temperature3, humidity3, temperature4, humidity4]
index = 2
sheet.insert_row(row, index)




## intereaction
# Let other programs interact with the data in a kinda hack-y but
# super simple way


## TEMPS
file = open('/var/www/html/tmp/CeilingTemp.txt', 'w')
file.write(temperature0 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone1Temp.txt', 'w')
file.write(temperature1 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone1Temp.txt', 'w')
file.write(temperature1 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone2Temp.txt', 'w')
file.write(temperature2 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone3Temp.txt', 'w')
file.write(temperature3 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone4Temp.txt', 'w')
file.write(temperature4 + "\n")
file.close()

## HUMIDITY
file = open('/var/www/html/tmp/CeilingHumd.txt', 'w')
file.write(humidity0 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone1Humd.txt', 'w')
file.write(humidity1 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone1Humd.txt', 'w')
file.write(humidity1 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone2Humd.txt', 'w')
file.write(humidity2 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone3Humd.txt', 'w')
file.write(humidity3 + "\n")
file.close()

file = open('/var/www/html/tmp/Zone4Humd.txt', 'w')
file.write(humidity4 + "\n")
file.close()








