#Simple Calulator
#Sophia Baker
#January 2018

import re
import numpy as np

#returns the pruduct (*) of two numbers
def multiply(num1,num2):
	return  num1 * num2

#returns the product (/) of two numbers
def divide(num1,num2):
	return  num1 / num2


#Strings call on operations to calulate mutliple variables using Regex
def sumAll(string):
	print("Addition & Subtraction:")
	for i in string:
		if i == '+' or i == '-' in string:
			#posList = re.findall("\+(\(?\d+\.?\d*\)?)",string)
			#negList = re.findall("(\-\(?\d+\.?\d*\)?)", string)
			List = re.findall("(\-?\(?\d+\.?\d*\)?)", string)
			#print("posList: " + str(posList))
			#print("negList: " + str(negList))
			print("firstNum: " + str(List))

			#posAnswer = sum(float(x) for x in posList)
			#negAnswer = sum(float(x) for x in negList)
			#print("posSum = " + str(posAnswer))
			#print("negSum = " + str(negAnswer))

			#answer1 = add(posAnswer,negAnswer)
			answer = sum(float(x) for x in List)
			#print(str(posAnswer) + " + " + str(negAnswer) + " = " + str(answer1))
			print("answer = " + str(answer))# + str(answer1) + " or " + str(answer))
			break #how do I make it only itterate once rather than having to break it
		else:
			print("no addition or subtraction")
			answer = string
			break
	return answer

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
	operation = "18.2+27/8*12/3+2*0.4+9"
else:
	operation = input("What calculation would you like to complete:")

#performing calulations in order of operation:	
operation1 = multiplyWhile(operation)
operation2 = divideWhile(operation1) #GET RID OF THE op.123 WHEN GET RID OF PRINTS
operation3 = sumAll(operation2)
print("answers:")
print(operation1)
print(operation2)
print(operation3)

print("the answer to your calculation is: " + str(operation3)) #EACH PIECE IS CORRECT BUT NOT WHEN TOGETHER!!!!!!

