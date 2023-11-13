import  RPi.GPIO as GPIO
import time
button_pin = ?
ledpin = ?
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    inputValue = GPIO.input(button_pin)
    if (inputValue == False):
        print("Button press ")
	GPIO.output(ledpin,GPIO.HIGH)
    	time.sleep(0.5)
    	GPIO.output(ledpin,GPIO.LOW)
    time.sleep(2)  // increase this parameter; observe the result
# Program for polling
