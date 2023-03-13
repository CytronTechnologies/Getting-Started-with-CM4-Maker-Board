import RPi.GPIO as GPIO
import time
import math

buttonPin1 = 17 #Define the button pins
buttonPin2 = 22
buttonPin3 = 27

buzzerPin = 19 #Define the buzzer pin

GPIO.setwarnings(False) #Disable warnings (optional)
GPIO.setmode(GPIO.BCM)  #Number GPIOs by Broadcom Chip

GPIO.setup(buzzerPin, GPIO.OUT) #Set buzzerPin's mode as output

GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin to be an input pin and set initial value to be pulled high
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

p = GPIO.PWM(buzzerPin, 1)
p.start(0);

def tone1():
    p.start(50)
    for x in range(0,361): #Frequency of the tone along the sine wave
        sinVal = math.sin(x * (math.pi / 180.0)) #Calculate the sine value
        toneVal = 2000 + sinVal * 500 #Add to the resonant frequency with a Weighted
        p.ChangeFrequency(toneVal) #Output PWM
        time.sleep(0.001)
        
def tone2():
    p.start(50)
    for x in range(0,361):
        sinVal = math.sin(x * (math.pi / 180.0))
        toneVal = 1000 + sinVal * 500
        p.ChangeFrequency(toneVal)
        time.sleep(0.001)
        
def tone3():
    p.start(50)
    for x in range(0,361):
        sinVal = math.sin(x * (math.pi / 180.0))
        toneVal = 3000 + sinVal * 800
        p.ChangeFrequency(toneVal)
        time.sleep(0.001)
        
def stopTone():
    p.stop()


while True: # Run forever

    if GPIO.input(buttonPin1) == GPIO.LOW:
        print("Button #17 was pushed!")
        tone1()
    elif GPIO.input(buttonPin2) == GPIO.LOW:
        print("Button #22 was pushed!")
        tone2()
    elif GPIO.input(buttonPin3) == GPIO.LOW:
        print("Button #27 was pushed!")
        tone3()
    else:
        stopTone()