import serial
ser = serial.Serial(“/dev/ttyACM0”, 9600) #/dev/tty/ACM0 is the serial port
#9600 is the baud rate and Arduino must be using the same value
s = [0, 1]  #use a list to store the input data from serial port
while True:
	read_serial = ser.readline() #read data from serial input
	s[0] = int (read_serial.rstrip()) #convert the input to an integer
	print(s[0])
	#print read_serial

# Program for Python reading data from Arduino 
