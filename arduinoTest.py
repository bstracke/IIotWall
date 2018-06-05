#!/usr/bin/python3


import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()
ser.open()

commands = {"1" : "triangle\n" ,"2" : "staticValue\n" ,"3" : "minMax\n" }

# read from Arduino

#inputRead = ser.read()

#print ("Read input " + inputRead.decode("utf-8") + " from Arduino")



# write 
print("Please type in command: ")
print("[1] triangle")
print("[2] staticValue")
print("[3] minMax")


eingabe = input("Eingabe: ")

if eingabe.isdigit() :
	ser.write(commands[eingabe].encode())
	
	
	if int(eingabe) == 2:
		print("Please input a value between 4-20mA: ")
		eingabe = input("Eingabe: ")
		ser.write(eingabe.encode())

else :
		println("No command")

# read response back from Arduino
while True:
	inputRead = ser.read(5)

	print ("Read input back: " + str(inputRead))

ser.close()	
