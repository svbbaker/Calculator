#Simple Calulator
#Sophia Baker
#January 2018

import re

#Strings call on operations to calulate mutliple variables using Regex:
#Exponents
def exp(string):
	print("Exponents:")
	while '^' in string:
		var1 = re.findall("(\(?\d+\.?\d*\)?)\^",string)[0]
		var2 = re.findall("\^(\(?\d+\.?\d*\)?)",string)[0]

		#print("var1 = " + var1)
		#print("var2 = " + var2)

		answer = float(var1) ** float(var2)
		#print("answer = " + str(answer))
		
		string = string.replace(var1 + "^" + var2, str(answer))

		#print("string = " + string)

	print("string = " + string)

	return string

#Multiplication and Division
def md(string):
	print("Multiplication & Division:")
	while '*' in string or '/' in string:
		var1 = re.findall("(\-?\(?\d+\.?\d*\)?)[\*\/]",string)[0]
		var2 = re.findall("[\*\/](\-?\(?\d+\.?\d*\)?)",string)[0]
		operator = re.findall("[\*\/]",string)[0]

		#print("var1 = " + var1)
		#print("var2 = " + var2)
		#print("operation: " + operator)

		if operator == '*':
			answer = float(var1) * float(var2)
			#print("answer = " + str(answer))
		elif operator == '/':
			answer = float(var1)/float(var2)
			#print("answer = " + str(answer))
		
		string = string.replace(var1 + operator + var2, str(answer))
		#print("string = " + string)

	print("string = " + string)

	return string

#Addition and Subtraction
def sumAll(string):
	print("Addition & Subtraction:")
	if '+' in string or '-' in string:
		for i in string:
			if i == '+' in string or i == '-' in string:
				line = re.findall("(\-?\d\.?\d*e\+\d+|\-?\(?\d+\.?\d*\)?)", string)
				print("List: " + str(line))
				answer = sum(float(x) for x in line)
				print("answer = " + str(answer))
				break
	else:
		print("no Multiplication or Division")
		answer = string
	
	return answer

#Parenthisis
def parenth(string):
	print("Parenthisis:")
	while '(' in string or ')' in string:
		part = re.findall("\(([^\)]+)\)",string)[0]
		print("part: " + part)

		
		answer = parenth(part)
		answer = exp(answer)
		answer = md(answer)
		answer = sumAll(answer)
		
		string = string.replace("(" + part + ")", str(answer))

	print("string = " + string)

	return string

#Solving for x
def solveX(string):
	print("Solving for x")


	print("string = " + string)

	return string


print("welcome to calculator.py")

#inputs
debug = True

if debug:
	operation = "1.4e+6+15-3"
else:
	operation = input("What calculation would you like to complete:")

#performing calulations in order of operation:	
operation = parenth(operation)
operation = exp(operation)
operation = md(operation)
operation = sumAll(operation)

print("the answer to your calculation is: " + str(operation))
