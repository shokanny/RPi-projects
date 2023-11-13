5.	import  RPi.GPIO as GPIO
6.	import time
7.	GPIO.setmode(GPIO.BCM)
8.	button_pin = ?
9.	ledpin = ?
10.	GPIO.setup(button_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
11.	GPIO.setup(ledpin, GPIO.OUT)
12.	GPIO.output(ledpin,GPIO.LOW)
13.	# this is similar to the ISR interrupt service routine
14.	def isr_callback(channel):
15.		GPIO.output(ledpin,GPIO.HIGH)
16.		Time.sleep(0.1)
17.		GPIO.output(ledpin,GPIO.LOW)
18.	
19.	GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=isr_callback)
20.	while True:
21.	   #add your codes to control the 8x8 display
