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


#Arrays call on caluculatons, to calulate mutliple variables:
def addWhile(string):
	return add(1,2)

def subtractWhile(string):
	return subtract(1,2)

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


debug = True

if debug:
	operation = "18.2-93/2*2.5+21*5-2"
else:
	operation = input("What calculation would you like to complete:")

#performing calulations in order of operation:	
operation = multiplyWhile(operation)
operation = divideWhile(operation)

