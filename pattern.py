import spidev
import time
spi=spidev.SpiDev()
spi.open(0,0)  #select the SPI device use spi.open(0,1) if connected to SPICE1
spi.max_speed_hz = 7629 # speed of the SPI clock
# use an array to store the LED pattern
# the first value is the row so it is from 1 to 8 
# the second value is used to form the pattern in the display 
pattern1 = [0x181, 0x242, 0x324, 0x400, 0x500, 0x624, 0x742, 0x881]
pattern2 = [0x1E7, 0x286, 0x386, 0x4E7, 0x581, 0x681, 0x787, 0x800]
#define a function to send 2 bytes
def write_pot(input):
	msb = input>>8   #shift the value 8 bits left so the row number is stored in msb
	lsb = input&0xff  #using binary AND to extract the ON OFF pattern to lsb
	spi.xfer([msb,lsb])  # send the data based on spi mechanism
#initialize the dot matrix display 
write_pot(0xb07)
time.sleep(0.5)
write_pot(0x900)
time.sleep(0.5)
write_pot(0xC01)
time.sleep(0.5)
write_pot(0xF00)
time.sleep(0.5)
counter = 0
while True:
   if counter % 2 == 0:
       for x in pattern1:
           write_pot(x)
           time.sleep(0.1)
   else:
       for x in pattern2:
           write_pot(x)
           time.sleep(0.1)
   counter += 1
#Program for SPI dot matrix display


# * * * 0 0 * * *  == 0xE7
# * 0 0 0 0 * 0 0  == 0x86
# * 0 0 0 0 * 0 0  == 0x86
# * * * 0 0 * * *  == 0xE7
# * 0 0 0 0 0 0 *  == 0x81
# * 0 0 0 0 0 0 *  == 0x81
# * 0 0 0 0 * * *  == 0x87
# 0 0 0 0 0 0 0 0  == 0x00
