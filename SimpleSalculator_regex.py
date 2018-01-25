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
	return add(float(array[0]),float(array[1]))

def subtractArray(array):
	return subtract(float(array[0]),float(array[1]))

def multiplyArray(array):
	return multiply(float(array[0]),float(array[1]))

def divideArray(array):
	return divide(float(array[0]),float(array[1]))


#main() calls on calculations
def main():
	
	debug = True

	if debug:
		operation = "18.2-93/2*2.5+21*5-2" #does not work for more than 1 multiplication sign but not for one either
	else:
		operation = input("What calculation would you like to complete:") #or raw_input ?

	while '*' in operation:
		firstMultiplier = re.findall("(\(?\d+\.?\d*\)?)\*",operation)[0]
		secondMultiplier = re.findall("\*(\(?\d+\.?\d*\)?)",operation)[0]

		print(firstMultiplier)
		print(secondMultiplier)

		answer = multiply(float(firstMultiplier),float(secondMultiplier))
		print(answer)
		operation = operation.replace(firstMultiplier + "*" + secondMultiplier, str(answer))

	return operation

	
	 
#Calling on funtion main()
print(main())

