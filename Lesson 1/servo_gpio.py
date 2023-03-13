import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)     #Number GPIOs by Broadcom Chip
GPIO.setup(13, GPIO.OUT)   #Set signal pin for the servo

pwm=GPIO.PWM(13, 50)
pwm.start(0)

while True:   
    pwm.ChangeDutyCycle(5) # left -90 deg position
    sleep(1)
    pwm.ChangeDutyCycle(7.5) # neutral position
    sleep(1)
    pwm.ChangeDutyCycle(10) # right +90 deg position
    sleep(1)
    pwm.ChangeDutyCycle(7.5) # neutral position
    sleep(1)
