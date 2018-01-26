#Simple Calulator
#Sophia Baker
#January 2018

import re

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


#Strings call on operations to calulate mutliple variables using Regex
def addWhile(string):
	print("Addition:")
	while '+' in string:
		firstAdder = re.findall("(\(?\d+\.?\d*\)?)\+",string)[0]
		secondAdder = re.findall("\+(\(?\d+\.?\d*\)?)",string)[0]

		print("var1 = " + firstAdder)
		print("var2 = " + secondAdder)

		answer = add(float(firstAdder),float(secondAdder))
		print("answer = " + str(answer))
		string = string.replace(firstAdder + "+" + secondAdder, str(answer))
		print("string = " + string)

	return string

def subtractWhile(string): #MINUS SIGNS...? 
	print("Subtract:")
	while '-' in string:
		firstSubtractor = re.findall("(\(?\d+\.?\d*\)?)\-",string)[0]
		secondSubtractor = re.findall("\-(\(?\d+\.?\d*\)?)",string)[0]

		print("var1 = " + firstSubtractor)
		print("var2 = " + secondSubtractor)

		answer = subtract(float(firstSubtractor),float(secondSubtractor))
		print("answer = " + str(answer))
		string = string.replace(firstSubtractor + "-" + secondSubtractor, str(answer))
		print("string = " + string)

	return string

def multiplyWhile(string):
	print("Multiplication:")
	while '*' in string:
		firstMultiplier = re.findall("(\(?\d+\.?\d*\)?)\*",string)[0]
		secondMultiplier = re.findall("\*(\(?\d+\.?\d*\)?)",string)[0]

		print("var1 = " + firstMultiplier)
		print("var2 = " + secondMultiplier)

		answer = multiply(float(firstMultiplier),float(secondMultiplier))
		print("answer = " + str(answer))
		string = string.replace(firstMultiplier + "*" + secondMultiplier, str(answer))
		print("string = " + string)

	return string

def divideWhile(string):
	print("Division:")
	while '/' in string:
		firstDivider = re.findall("(\(?\d+\.?\d*\)?)\/",string)[0]
		secondDivider = re.findall("\/(\(?\d+\.?\d*\)?)",string)[0]

		print("var1 = " + firstDivider)
		print("var2 = " + secondDivider)

		answer = divide(float(firstDivider),float(secondDivider))
		print("answer = " + str(answer))
		string = string.replace(firstDivider + "/" + secondDivider, str(answer))
		print("string = " + string)

	return string

	
print("welcome to calculator.py")

#inputs
debug = True

if debug:
	operation = "18.2-93/2*2.5+21*5-2+5"
else:
	operation = input("What calculation would you like to complete:")

#performing calulations in order of operation:	
operation = multiplyWhile(operation)
operation = divideWhile(operation)
print("the answer to your calculation is: " + operation)

