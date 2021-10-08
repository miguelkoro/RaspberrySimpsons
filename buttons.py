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

    #Medir las pulsaciones 
while (True):
    input = GPIO.input(26)
    start = time.time()
    stop = time.time()
    while GPIO.input(pin) == 0:
        start = time.time()
    while GPIO.input(pin) == 1
        stop = time.time()
    elapsed = stop - start    
    if elapsed > 2: # se mantiene el boton mas de 2seg        
        os.system("shutdown now")
    else:
        os.system("killall omxplayer")
    time.sleep(0.3)
