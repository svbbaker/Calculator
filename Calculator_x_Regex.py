#Simple Calulator
#Sophia Baker
#January/February 2018

#Regex
import re

#################################################################################################################

#Exponents
def expo(string):
	print("Exponents:")
	while '^' in string:
		var1 = re.findall("(\(?\d+\.?\d*\)?)\^",string)[0] #^[\e\+\d+]
		var2 = re.findall("\^(\(?\d+\.?\d*\)?)",string)[0]

		print("var1 = " + var1)
		print("var2 = " + var2)

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
		answer = expo(answer)
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

#variable multiplicaiton
def varMulComb(input1,input2):
	print("Variable Combined Multiplicaiton:")

	exp = 0
	coef = 1

	#if variables
	if re.findall("([a-z])",input1): #if input1 has a variable
		var = re.findall("([a-z])",input1)[0] #then it is equal to var
		g = True #and g is true
	else: #else
		num = input1 #input1 is equal to num
		g = False #and g is false
	if re.findall("([a-z])",input2): #if input2 has a variable
		var = re.findall("([a-z])",input2)[0] #then it is equal to var
		h = True #and h is true
	else: #else
		num = input2 #input2 is equal to num
		h = False #and h is false

	if g == True:
		variable = input1
	else: number = input1
	if h == True:
		variable = input2
	else: number = input2

	#replace -x with -1x
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var1)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var2)

	if g != h: #if they are not the same then there is a value for var and num
		#num of variable occerences
		exp = input1.count(var)
		#exponents
		if re.findall("\^(\-?\d+)",variable):
			n = re.findall("\^(\-?\d+)",variable)[0]
			n = float(n)
			exp = exp + n -1 #-1 so that we dont acount for an extera variable from count above
		if re.findall("(\d+\^[\-?\d+])",number):
			number = expo(number)
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",variable):
			n = re.findall("(?<![\^\-])[\-\d\.]+",variable)[0]
			n = float(n)
			coef = coef * n
		coef = coef * number
		a = "%s" %coef
		b = "%s" %var
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
		if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)",inside): #if *
			if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside): #if variables
				var1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/]",inside)[0]
				var2 = re.findall("[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside)[0]
				varA = expo(var1)
				varB = expo(var2)
				# HOW TO DEAL WITH 4^X * BLAH ?!??!?!?!?!?!?! here
				part = varMul(varA,varB)
				inside = inside.replace(var1 + "*" + var2, str(part))
				#print("new inside:")
				#print(inside)
			if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*)|(\-?\d+\.?\d*\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside): #if mixed variables
				#print("part:")
				#print(re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",inside)) 
				var1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)[\*\/]",inside)[0]
				#print(var1)
				var2 = re.findall("[\*\/](\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)",inside)[0]
				#print(var2)
				varA = expo(var1)
				varB = expo(var2)
				# HOW TO DEAL WITH 4^x * BLAH ?!??!?!?!?!?!?! here
				part = varMulComb(varA,varB)
				#print(part)
				inside = inside.replace(var1 + "*" + var2, str(part))
				print("new inside:")
				print(inside)
			#print("inside:")
			#print(re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*)",inside))
			if re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/](\-?\d+\.?\d*\^?\d*)",inside): #if variables 
				var1 = re.findall("(\-?\d+\.?\d*\^?\d*)[\*\/]",inside)[0]
				var2 = re.findall("[\*\/](\-?\d+\.?\d*\^?\d*)",inside)[0]
				varA = expo(var1)
				varB = expo(var2)
				part = varA + "*" + varB
				part = md(part)
				inside = inside.replace(var1 + "*" + var2, str(part))
				return inside
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
#operation = expo(operation)
#operation = md(operation)
#operation = sumAll(operation)

#print("the answer to your calculation is: " + str(operation))

function = '5(5^2x*2x+2*3^2+2x^2*5^2)'
#function = distrib(function)

#inputs
a = '2^2'
b = '5'
#print(varMul(a,b))
#print(varDiv(a,b))
#print(varAdd(a,b))
#print(varSub(a,b))

x = "x^2"
y = "3^2"
varMulComb(x,y)
#print(y)
#expo(y)


