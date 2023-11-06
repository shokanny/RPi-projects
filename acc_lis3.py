import sys
sys.path.append('/home/pi/Pi_lab')
import LIS3DH
import time, spidev, sys, smbus
import RPi.GPIO as GPIO

asensor = LIS3DH.Accelerometer('i2c', i2cAddress = 0x19)
asensor.set_ODR(odr=50, powerMode='normal')
asensor.axis_enable(x='on',y='on',z='on')
asensor.set_BDU('on')
asensor.set_scale()
GPIO.setmode(GPIO.BCM)

while True:
    try:
        while True:
            x = asensor.x_axis_reading()
            y = asensor.y_axis_reading()
            print('x: '+str(x)+' y: '+str(y))
            time.sleep(2)
    except:
        print('stop reading')
        break
    
del(asensor)