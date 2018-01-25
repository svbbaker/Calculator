import re


print("welcome to calculator.py")

#returns the summ of two numbers
def add(num1,num2):
	return  num1 + num2

#returns the difference of two numbers
def subtract(num1,num2):
	return  num1 - num2

#returns the pruduct (*) of two numbers
def multiply(num1,num2):
	return  num1 * num2

#returns the product (/) of two numbers
def divide(num1,num2):
	return  num1 / num2

#Arrays call on caluculatons, to calulate mutliple variables:
def addArray(array):
	return add(int(array[0]),int(array[1]))

def subtractArray(array):
	return subtract(int(array[0]),int(array[1]))

def multiplyArray(array):
	#for i in range(0,5) #between the numer or parts of the array - NEEDS WORK
	return multiply(int(array[0]),int(array[1]))
#def multiplyArray(array): #mutiply the pieces in the array (take it as an int not as a sting)
	#for i in range(0,5):#between the numer or parts of the array
	#return multiply(int(array[0]),int(array[1])

def divideArray(array):
	return divide(int(array[0]),int(array[1]))


#main() calls on calculations
def main():
	
	debug = True

	if debug:
		operation = "18.2-93/2*2.5+21*5-2" #does not work for more than 1 multiplication sign but not for one either
	else:
		operation = input("What calculation would you like to complete:") #or raw_input ?

	while '*':
		firstMultiplier = re.findall("\(?\d+\.?\d+\)?\*",operation)[0]
		secondMultiplier = re.findall("\*\(?\d+\.?\d+\)?",operation)[0]
		answer = 0
		
		print(firstMultiplier)
		print(secondMultiplier)

		answer = multiply(firstMultiplier,secondMultiplier)

		newstring = operation.replace("\(?\d+\.?\d+\)?\*"+"\*\(?\d+\.?\d+\)?", answer)

		return newstring

	result = 1

	return result
	 
#Calling on funtion main()
print(main())

