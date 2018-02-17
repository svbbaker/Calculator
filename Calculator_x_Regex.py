#Simple Calulator
#Sophia Baker
#January/February 2018

#Regex
import re

#################################################################################################################

#Exponents
def exp(string):
	print("Exponents:")
	while '^' in string:
		var1 = re.findall("(\(?\d+\.?\d*\)?)\^",string)[0] #^[\e\+\d+]
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
	#print("Multiplication & Division:")
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

	#print("string = " + string)

	return string

#Addition and Subtraction
def sumAll(string):
	#print("Addition & Subtraction:")
	if '+' in string or '-' in string:
		for i in string:
			if i == '+' in string or i == '-' in string:
				line = re.findall("(\-?\d\.?\d*e\+\d+|\-?\(?\d+\.?\d*\)?)", string)
				#print("List: " + str(line))
				answer = sum(float(x) for x in line)
				#äprint("answer = " + str(answer))
				break
	else:
		#print("no Multiplication or Division")
		answer = string
	
	return answer

#Parenthisis
def parenth(string):
	#print("Parenthisis:")
	while '(' in string or ')' in string:
		part = re.findall("\(([^\)]+)\)",string)[0]
		print("part: " + part)

		
		answer = parenth(part)
		answer = exp(answer)
		answer = md(answer)
		answer = sumAll(answer)
		
		string = string.replace("(" + part + ")", str(answer))

	#print("string = " + string)

	return string

#################################################################################################################

#variables
#variable multiplicaiton
def varMul(input1,input2):
	print("Variable Multiplicaiton:")

	exp = 0
	coef = 1

	#if variables
	if re.findall("([a-z])",input1):
		var1 = re.findall("([a-z])",input1)[0]
	else: var1 = False
	if re.findall("([a-z])",input2):
		var2 = re.findall("([a-z])",input2)[0]
	else: var2 = True

	#replace -x with -1x
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var1)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var2)

	if var1 == var2:
		#num of variable occerences
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		exp = exp1 + exp2
		#exponents
		if re.findall("\^(\-?\d+)",input1):
			num = re.findall("\^(\-?\d+)",input1)[0]
			num = float(num)
			exp = exp + num -1 #-1 so that we dont acount for an extera variable from count above
		if re.findall("\^(\-?\d+)",input2):
			num = re.findall("\^(\-?\d+)",input2)[0]
			num = float(num)
			exp = exp + num -1
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef * num
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef * num
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp
		answer = a+b+c

	else:
		answer = False	

	return answer

#variable Division
def varDiv(input1,input2):
	print("Variable Division:")

	exp = 0
	coef = 1
	
	#if variables
	if re.findall("([a-z])",input1):
		var1 = re.findall("([a-z])",input1)[0]
	if re.findall("([a-z])",input2):
		var2 = re.findall("([a-z])",input2)[0]

	#replace -x with -1x
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var1)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var2)

	if var1 == var2:
		#num of variable occerences
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		#exponents
		if re.findall("\^(\-?\d+)",input1):
			num = re.findall("\^(\-?\d+)",input1)[0]
			num = float(num)
			expA = exp1 + num -1 #-1 so that we dont acount for an extera variable from count above
		else: expA = exp1
		if re.findall("\^(\-?\d+)",input2):
			num = re.findall("\^(\-?\d+)",input2)[0]
			num = float(num)
			expB = exp2 + num -1
		else: expB = exp2
		exp = expA - expB
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef / num
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp
		answer = a+b+c
	else: 
		answer = False #"False"
	return answer

#variable Addition
def varAdd(input1,input2):
	print("Variable Addition:")

	coef = 0
	
	#if variables
	if re.findall("([a-z])",input1):
		var1 = re.findall("([a-z])",input1)[0]
	if re.findall("([a-z])",input2):
		var2 = re.findall("([a-z])",input2)[0]

	if re.findall("\^(\-?\d+)",input1):
		exp1 = re.findall("\^(\-?\d+)",input1)[0]
	else: exp1 = True
	if re.findall("\^(\-?\d+)",input2):
		exp2 = re.findall("\^(\-?\d+)",input2)[0]
	else: exp2 = True

	#replace -x with -1x
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var1)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var2)

	if var1 == var2 and exp1 == exp2:
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef + num 
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef + num
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp1
		answer = a+b+c

	else:
		answer = False

	return answer

#variable Addition
def varSub(input1,input2):
	print("Variable Subtraction:")

	coef = 0
	
	#if variables
	if re.findall("([a-z])",input1):
		var1 = re.findall("([a-z])",input1)[0]
	if re.findall("([a-z])",input2):
		var2 = re.findall("([a-z])",input2)[0]

	if re.findall("\^(\-?\d+)",input1):
		exp1 = re.findall("\^(\-?\d+)",input1)[0]
	else: exp1 = True
	if re.findall("\^(\-?\d+)",input2):
		exp2 = re.findall("\^(\-?\d+)",input2)[0]
	else: exp2 = True

	#replace -x with -1x
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var1)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var2)

	if var1 == var2 and exp1 == exp2:
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef + num 
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef - num
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp1
		answer = a+b+c

	else:
		answer = False

	return answer

#################################################################################################################

def distrib(string):
	print("Distributive Property:")
	if re.findall("((\-?\d+?[a-z]|\-?\d)\((.+)\))",string):
		inside = re.findall("\((.+)\)",string)[0]
		#print(inside)
		#print("inside:")
		#print(re.findall("(\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)",inside))
		if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)",inside): #if *
			if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside): #if variables
				#print("part:")
				#print(re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside)) 
				var1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/]",inside)[0]
				#print(var1)
				var2 = re.findall("[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside)[0]
				#print(var2)
				varA = exp(var1)
				#print(varA)
				varB = exp(var2)
				#print(varB)
				# HOW TO DEAL WITH 4^X * BLAH ?!??!?!?!?!?!?! here
				part = varMul(varA,varB)
				#print(part)
				inside = inside.replace(var1 + "*" + var2, str(part))
				print("new inside:")
				print(inside)
			#IF MIXED
			print("inside:")
			print(re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*)",inside))
			if re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*)",inside): #if variables
				print("part:")
				print(re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*)",inside)) 
				var1 = re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/]",inside)[0]
				print(var1)
				var2 = re.findall("[\*\/](\-?\d+\.?\d*\^?\d*)",inside)[0]
				print(var2)
				varA = exp(var1)
				print(varA)
				varB = exp(var2)
				print(varB)
				part = varA + "*" + varB
				print("part")
				print(part)
				part = md(part)
				print(part)
				print(inside)
				print(var1)
				print(var2)
				inside = inside.replace(var1 + "*" + var2, str(part))
				print("inside:")
				print(inside)
				return inside
			
		#multiply the piece before the parenth interativly through the pieces inside the parenths
		answer = True
		print(answer)
	return answer


#################################################################################################################
print("welcome to calculator.py")

#inputs
debug = True

if debug:
	operation = '2^2*5'
else:
	operation = input("What calculation would you like to complete:")

#performing calulations in order of operation:	
#operation = parenth(operation)
#operation = exp(operation)
#operation = md(operation)
#operation = sumAll(operation)

#print("the answer to your calculation is: " + str(operation))

function = '5(5^2x*2x+2*3^2)'
function = distrib(function)

#inputs
a = '2^2'
b = '5'
#print(varMul(a,b))
#print(varDiv(a,b))
#print(varAdd(a,b))
#print(varSub(a,b))

