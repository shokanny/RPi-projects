import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
button_pin = ?
ledpin = ?
GPIO.setup(button_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.output(ledpin,GPIO.LOW)
# this is similar to the ISR interrupt service routine
def isr_callback(channel):
	GPIO.output(ledpin,GPIO.HIGH)
	Time.sleep(0.1)
	GPIO.output(ledpin,GPIO.LOW)

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=isr_callback)
while True:
   time.sleep(5)
    # The interrupt program 
