import RPi.GPIO as GPIO
import time
import os

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)

def turnOnScreen():
    os.system('raspi-gpio set 19 op a5')
    GPIO.output(18, GPIO.HIGH)

turnOnScreen()
    
while (True):
    input = GPIO.input(26)
    if input == True:
        print("Pulsacion")
        time.sleep(2.0)
        if input == True:
            print(" Larga")
        else:
            print(" Corta")
    time.sleep(0.3)
