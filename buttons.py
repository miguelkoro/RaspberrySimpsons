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

#Otra forma
#while True:
            # set an interrupt on a falling edge and wait for it to happen
    #GPIO.wait_for_edge(INT, GPIO.FALLING)
            # we got here because the button was pressed.
            # wait for 3 seconds to see if this was deliberate
    #sleep(3)
            # check the button level again
    #if GPIO.input(INT) == 0:
                # still pressed, it must be a serious request; shutdown Pi
        #subprocess.call(['poweroff'], shell=True, \
            #stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#otra forma
#def push_button():
#    start_time=time.time()
#    diff=0

#    while button1.is_active and (diff <hold_time) :
#        now_time=time.time()
#        diff=-start_time+now_time

#    if diff < hold_time :
#        small_alarm()
#    else:
#        long_push()


    #Medir las pulsaciones 
#start = time.time()
#stop = time.time()
#while GPIO.input(pin) == 0:
#    start = time.time()
#while GPIO.input(pin) == 1
#    stop = time.time()
#elapsed = stop - start

while (True):
    input = GPIO.input(26)
    if input == GPIO.LOW:
        print("Pulsacion")
        time.sleep(2.0)
        if input == True:
            print(" Larga")
        else:
            print(" Corta")
    time.sleep(0.3)
