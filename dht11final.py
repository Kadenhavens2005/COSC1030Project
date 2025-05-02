import time
import adafruit_dht
import board
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
#while True:
GPIO.output(14, GPIO.HIGH)
sleep(1)
GPIO.output(14, GPIO.LOW)
sleep(1)
dht_device = adafruit_dht.DHT11(board.D4)
while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9/5) +32

        humidity = dht_device.humidity

        print(" =Temp:{:.1f} c / {:.1f} F   Humidity: {}%".format(temperature_c,temperature_f, humidity))
 
        if temperature_f > 77: 
            GPIO.output(14, GPIO.HIGH)
       # time.sleep(2.0)
        else:
            GPIO.output(14,GPIO.LOW)
        time.sleep(2.0)
    except:
         print("FAILED TO GATHER DATA AT THIS TIME")


