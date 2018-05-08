#Calulator
#Sophia Baker
#Independant Competer Science
#Mr. Guillaume Sparrow-Peppin
#2018

#Regex
import re

#selects term with exponents (ex: 3.2x^2y )
TERM = "\-?\d*\.?\d*[a-z]*\^?\-?\d*\.?\d*[a-z]?"

#############################################################################################################################################################################################
#############################################################################################################################################################################################
#NUMBERS

#Multiplication and Division (only applicable if no * of / in string)
def md(string):
	#print("Multiplication & Division:")
	#if there is a * or / in the input string then run loop until there is not another
	while '*' in string or '/' in string:
		#variable 1: part before the * or / symbol
		var1 = re.findall("(\-?\(?\d+\.?\d*\)?)[\*\/]",string)[0]
		#variable 2: part after the * or / symbol
		var2 = re.findall("[\*\/](\-?\(?\d+\.?\d*\)?)",string)[0]
		#what symbol is between the variabeles: * or /
		operator = re.findall("[\*\/]",string)[0]
		#if multiplication:
		if operator == '*':
			answer = float(var1) * float(var2)
		#else if division:
		elif operator == '/':
			answer = float(var1)/float(var2)
		#replace the part in input string (var1 sybol var2) with the answer from the operation
		string = string.replace(var1 + operator + var2, str(answer))

	#return the new string
	return string

#Addition and Subtraction
def sumNums(string):
	#print("Addition & Subtraction:")
	#adds plus to string in order to enable creating final string as the last step of sumNums
	string = "+" + string
	#finding all the pieces in the string
	pieces = re.findall("([+-]?\d+[a-z]?)",string)
	#string for variables
	variables = ""
	#sorts out variables in pieces and creats new string with variables
	#creats an intterative piece of pieces
	for piece in pieces:
		#if there is a variable piece
		if re.findall("[a-z]",piece):
			#creats new string with pieces 
			variables += piece
			#remove the pice (if it contains a variable)
			pieces.remove(piece)
	#sumes pieces
	answer = sum(float(a) for a in pieces)
	#enabels adding answer to string
	z = "%s" %answer
	#update string with answer for all added numbers attated to front of variable string
	string = z + variables
	return string

#Parenthisis
def parenth(string):
	#print("Parenthisis:")
	#if there are parenthisis in the input string then run loop until there is not another
	while '(' in string or ')' in string:
		#part: part of the input string inbetween the parenthisis - (...)
		part = re.findall("\(([^\)]+)\)",string)[0]
		
		#answer: part solved by going through exponent, multiplication, addition
		answer = parenth(part)
		answer = exponent(answer)
		answer = multiplication(answer)
		answer = sumNums(answer)
		
		#replace the part in input string inside the parenthisis inclusive, with the answer from the operation itteration
		string = string.replace("(" + part + ")", str(answer))

	#return the new string
	return string


#############################################################################################################################################################################################
#############################################################################################################################################################################################
#VARIABLS

# HOW TO DEAL WITH 4^x * BLAH ?!??!?!?!?!?!?! here

#variable multiplicaiton
def varMul(input1,input2):
	#print("Variable Multiplicaiton:")

	#defining variables: exponent initialy 0, coefficient initially 1 ('cause multiplication)
	exp = 0
	coef = 1

	#if variables
	if re.findall("([a-z])",input1):
		#var1: variable in input1
		var1 = re.findall("([a-z])",input1)[0]
	#if no variable in input1 then var1 is false
	else: var1 = False
	if re.findall("([a-z])",input2):
		#var2: variable in input2
		var2 = re.findall("([a-z])",input2)[0]
	#if no variable in input 2 than var2 us false
	else: var2 = True

	#replace -x with -1x (in both input1 and input 2)
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var1)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var2)

	#if the variables in input1 and input2 are equal:
	if var1 == var2:
		#num of variable occerences (exp1 correnlates to var1 and exp2 to variable2)
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		#exp is equal to the sum of variale occerences in var1 and var2 (denoted as exp1 and exp2)
		exp = exp1 + exp2
		#exponents
		#if there is ^ in input1
		if re.findall("\^(\-?\d+)",input1):
			#select the piece that is after the ^ 
			num = re.findall("\^(\-?\d+|\(.+\))",input1)[0]
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#exp is equal to the former exp value sumed with num, -1 subtracts the extera variable acounted for in the variable amount count
			exp = exp + num -1
		#if there is ^ in input2		
		if re.findall("\^(\-?\d+)",input2):
			#select the piece that is after the ^ 
			num = re.findall("\^(\-?\d+|\(.+\))",input2)[0]
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#exp is equal to the former exp value sumed with num, -1 subtracts the extera variable acounted for in the variable amount count
			exp = exp + num -1
		#coeffients
		#if there is a number before the variable in input1
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			#num is equal to the number before the variable
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#coef is equal to former coef times the number before the variable - num -
			coef = coef * num
		#if there is a number before the variable in input2
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			#num is equal to the number before the variable
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]			
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#coef is equal to former coef times the number before the variable - num -
			coef = coef * num
		#creating variables = strings that are variables	
		#coeffiencet value
		a = "%s" %coef 
		#the variable being used (looking to var1 to find which letter it is)
		b = "%s" %var1
		#extopenet value including ^ (exponent) symbol
		c = "^%s" %exp
		#answer: combined variables holding the variable parts as strings
		answer = a+b+c

	#if the variables in input1 and input2 are not equal:
	if var1 != var2:
		#num of variable occerences (exp1 correnlates to var1 and exp2 to variable2)
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		#exponents
		#if there is ^ in input1
		if re.findall("\^(\-?\d+)",input1):
			#select the piece that is after the ^ 
			num = re.findall("\^(\-?\d+|\(.+\))",input1)[0]
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#exp is equal to the former exp value sumed with num, -1 subtracts the extera variable acounted for in the variable amount count
			exp1 = exp1 + num -1
		#if there is ^ in input2		
		if re.findall("\^(\-?\d+)",input2):
			#select the piece that is after the ^ 
			num = re.findall("\^(\-?\d+|\(.+\))",input2)[0]
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#exp is equal to the former exp value sumed with num, -1 subtracts the extera variable acounted for in the variable amount count
			exp2 = exp2 + num -1
		#coeffients
		#if there is a number before the variable in input1
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			#num is equal to the number before the variable
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#coef is equal to former coef times the number before the variable - num -
			coef = coef * num
		#if there is a number before the variable in input2
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			#num is equal to the number before the variable
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]			
			#if there are parenthisis symplify the inside
			num = parenth(num)
			#makes num into numbers with decimals
			num = float(num)
			#coef is equal to former coef times the number before the variable - num -
			coef = coef * num
		#creating variables = strings that are variables	
		#coeffiencet value
		a = "%s" %coef 
		#the variable 1
		b = "%s" %var1
		#extopenet value including ^ (exponent) symbol for variabel 1
		c = "^%s" %exp1
		#the variable 2
		d = "%s" %var2
		#extopenet value including ^ (exponent) symbol for variabel 2
		e = "^%s" %exp2
		#answer: combined variables holding the variable parts as strings
		answer = a+b+c+d+e

	#returning answer
	return answer

#variable Division
def varDiv(input1,input2):
	#print("Variable Division:")

	#defining variables: exponent initialy 0, coefficient initially 1 ('cause multiplication)
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

	#if variables are equall
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
			coef = coef * num
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef / num
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp
		answer = a+b+c

	#if variables are not equall
	if var1 != var2:
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
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef * num
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef / num
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %expA
		d = "%s" %var2
		e = "^%s" %expB
		answer = a+b+c+d+e

	return answer

#variable Addition
def varAdd(input1,input2):
	#print("Variable Addition:")

	coef = 0
	
	#if variables
	if re.findall("([a-z])",input1):
		var1 = re.findall("([a-z])",input1)[0]
	if re.findall("([a-z])",input2):
		var2 = re.findall("([a-z])",input2)[0]

	if re.findall("\^(\-?\d+)",input1):
		exp1 = re.findall("\^(\-?\d+)",input1)[0]
	else: exp1 = 1
	if re.findall("\^(\-?\d+)",input2):
		exp2 = re.findall("\^(\-?\d+)",input2)[0]
	else: exp2 = 1

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
		a = "%s" %input1
		b = "%s" %input2
		answer = a + "+" + b

	return answer

#variable Addition
def varSub(input1,input2):
	#print("Variable Subtraction:")

	coef = 0
	
	#if variables
	if re.findall("([a-z])",input1):
		var1 = re.findall("([a-z])",input1)[0]
	if re.findall("([a-z])",input2):
		var2 = re.findall("([a-z])",input2)[0]

	if re.findall("\^(\-?\d+)",input1):
		exp1 = re.findall("\^(\-?\d+)",input1)[0]
	else: exp1 = 1
	if re.findall("\^(\-?\d+)",input2):
		exp2 = re.findall("\^(\-?\d+)",input2)[0]
	else: exp2 = 1

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
		a = "%s" %input1
		b = "%s" %input2
		answer = a + "-" + b

	return answer


#############################################################################################################################################################################################
#############################################################################################################################################################################################
#MIXED

#variable combined multiplicaiton
def varMulComb(input1,input2):	#print("Variable Combined Multiplicaiton:")

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

	#replace -x with -1x
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var)

	if g == True:
		variable = input1
	else: number = input1
	if h == True:
		variable = input2
	else: number = input2


	if g != h: #if they are not the same then there is a value for var and num
		#exponents
		if re.findall("\^(\-?\d+)",variable):
			n = re.findall("\^(\-?\d+)",variable)[0]
			n = float(n)
			exp = exp + n 
		else: exp = 1

		if re.findall("(\d+\^[\-?\d+])",number):
			number = exponent(number)
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",variable):
			n = re.findall("(?<![\^\-])[\-\d\.]+",variable)[0]
			n = float(n)
			coef = coef * n
		coef = coef * float(number)
		a = "%s" %coef
		b = "%s" %var
		c = "^%s" %exp
		answer = a+b+c

	else:
		a = "%s" %input1
		b = "%s" %input2
		answer = a + "*" + b

	return answer

#variable combined division
def varDivComb(input1,input2):
	#print("Variable Combined Division:")

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

	#replace -x with -1x 
	if re.findall("(\-[a-z])",input1):
		input1 = input1.replace(str(re.findall("(\-[a-z])",input1)[0]), "-1%s"%var)
	if re.findall("(\-[a-z])",input2):
		input2 = input2.replace(str(re.findall("(\-[a-z])",input2)[0]), "-1%s"%var)

	if g == True:
		variable = input1
	else: number = input1
	if h == True:
		variable = input2
	else: number = input2

	#number of variable occerences
	exp = variable.count(var)
	#exponents
	if re.findall("\^(\-?\d+)",variable):
		n = re.findall("\^(\-?\d+)",variable)[0]
		n = float(n)
		if g == False:
			exp = (exp + n -1) #-1 so that we dont acount for an extera variable from count above
		if h == False:
			exp = exp + n - 1
	if re.findall("(\d+\^[\-?\d+])",number):
		number = exponent(number)
	#if no exponent (sill need to be able to account for an x in the denominator as x^-1 in the answer)
	if re.findall("(?<![\^\-])",variable):
		if g == False:
			exp = (-1) * exp
		if h == False:
			exp = exp
	#coeffients
	if re.findall("(?<![\^\-])[\-\d\.]+",variable):
		n = re.findall("(?<![\^\-])[\-\d\.]+",variable)[0]
		n = float(n)
		coef = coef * n
	#divide the coeffient before the polynomial and the number (depending on which one has the variable)
	if h == True:
		coef = float(number) / coef
	if g == True:
		coef = coef / float(number)

	a = "%s" %coef
	b = "%s" %var
	c = "^%s" %exp
	answer = a+b+c

	return answer


#############################################################################################################################################################################################
#############################################################################################################################################################################################
#COMBINED

#Exponents
def exponent(string):
	#print("Exponents:")
	while len(re.findall("(\(?\d+\.?\d*\)?)\^(\(?\d+\.?\d*\)?)",string))>0:
		var1 = re.findall("(\(?\d+\.?\d*\)?)\^",string)[0]
		var2 = re.findall("\^(\(?\d+\.?\d*\)?)",string)[0]
		answer = float(var1) ** float(var2)
		string = string.replace(var1 + "^" + var2, str(answer))
	return string

#Multiplicaiton
def multiplication(string):
	#while loop to make sure this is done correctly
	while re.findall("(\-[a-z])",string) or re.findall("\*[a-z]",string) or string[0] == re.findall("[a-z]",string)[0]:
		#replace -var with -1var
		if re.findall("(\-[a-z])",string):
			var = re.findall("\-([a-z])",string)[0]
			string = string.replace(str(re.findall("(\-[a-z])",string)[0]), "-1%s"%var)
		#replace var with 1var
		if re.findall("(\*[a-z])",string):
			var = re.findall("\*([a-z])",string)[0]
			string = string.replace(str(re.findall("(\*[a-z])",string)[0]), "*1%s"%var)
		#if first index is variable then replace it with 1var
		if string[0] == re.findall("[a-z]",string)[0]:
			var = string[0]
			string = "1%s"%var + string[1:]
	#return string
	while "*" in string:
		#if numbers
		if re.findall("(?<!\^)(\+?\-?\d*\.?\d+)\*(\+?\-?\d*\.?\d+)(?![a-z.\d+])",string):
			var1 = re.findall("(?<!\^)(\+?\-?\d*\.?\d+)\*\+?\-?\d*\.?\d+(?![a-z.\d+])",string)[0]
			var2 = re.findall("(?<!\^)\+?\-?\d*\.?\d+\*(\+?\-?\d*\.?\d+)(?![a-z.\d+])",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varA + "*" + varB
			part = md(part)
			string = string.replace(var1 + "*" + var2, str(part))
		#if variables
		if re.findall("(\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)[\*](\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)",string):
			var1 = re.findall("(?<![\^])(\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)[\*]\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*",string)[0]
			var2 = re.findall("\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*[\*](\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varMul(varA,varB)
			string = string.replace(var1 + "*" + var2, str(part))
		#if number and variable
		if re.findall("(\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)[\*](\-?\d+\.?\d*\^?\-?\d*\.?\d*)|(\-?\d+\.?\d*\^?\-?\d*\.?\d*)[\*](\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)",string):
			var1 = re.findall("(?<![\^])(\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)[\*]\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*",string)[0]
			var2 = re.findall("(?<![\^])\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*[\*](\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)",string)[0]
			#print("var1+2:",var1,var2)
			varA = exponent(var1)
			varB = exponent(var2)
			part = varMulComb(varA,varB)
			string = string.replace(var1 + "*" + var2, str(part))
			break
	return(string)

#Division
def division(string):
	while re.findall("(\-[a-z])",string) or re.findall("\/[a-z]",string) or string[0] == re.findall("[a-z]",string)[0]:
		#replace -var with -1var
		if re.findall("(\-[a-z])",string):
			var = re.findall("\-([a-z])",string)[0]
			string = string.replace(str(re.findall("(\-[a-z])",string)[0]), "-1%s"%var)
		#replace var with 1var
		if re.findall("(\/[a-z])",string):
			var = re.findall("\/([a-z])",string)[0]
			string = string.replace(str(re.findall("(\/[a-z])",string)[0]), "/1%s"%var)
		#if first index is variable then replace it with 1var
		if string[0] == re.findall("[a-z]",string)[0]:
			var = string[0]
			string = "1%s"%var + string[1:]
	#return string
	while "/" in string:
		#if numbers
		if re.findall("(?<!\^)(\+?\-?\d*\.?\d+)\/(\+?\-?\d*\.?\d+)(?![a-z.\d+])",string):
			var1 = re.findall("(?<!\^)(\+?\-?\d*\.?\d+)\/\+?\-?\d*\.?\d+(?![a-z.\d+])",string)[0]
			var2 = re.findall("(?<!\^)\+?\-?\d*\.?\d+\/(\+?\-?\d*\.?\d+)(?![a-z.\d+])",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varA + "/" + varB
			part = md(part)
			string = string.replace(var1 + "/" + var2, str(part))
		#if variables
		if re.findall("(\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)[\/](\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)",string):
			var1 = re.findall("(?<![\^])(\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)[\/]\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*",string)[0]
			var2 = re.findall("\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*[\/](\-?\d*\.?\d?[a-z]+\^?\-?\d*\.?\d*)",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varMul(varA,varB)
			string = string.replace(var1 + "/" + var2, str(part))
		#if number and variable
		if re.findall("(\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)[\/](\-?\d+\.?\d*\^?\-?\d*\.?\d*)|(\-?\d+\.?\d*\^?\-?\d*\.?\d*)[\/](\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)",string):
			var1 = re.findall("(?<![\^])(\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)[\/]\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*",string)[0]
			var2 = re.findall("(?<![\^])\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*[\/](\-?\d+\.?\d*\^?\-?\d*\.?\d*[a-z]?\^?\-?\d*\.?\d*)",string)[0]
			#print("var1+2:",var1,var2)
			varA = exponent(var1)
			varB = exponent(var2)
			part = varMulComb(varA,varB)
			string = string.replace(var1 + "/" + var2, str(part))
			break
	return(string)

#Summation
def summation(string):
	####need to sort it so that can solve 3x-9x+14-2+2x :: currently it can only do 3x-9x+14-2
	if re.findall(".(\-).",string):
		minus = True
	else: minus = False

	while "+" in string in string or minus == True:
		#if numbers 
		if re.findall("(?<!\^)(\+?\-?\d*\.?\d+)\*(\+?\-?\d*\.?\d+)(?![a-z.\d+])",string):
			string = sumNums(string)
		#if variables +
		if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\+](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string):
			input1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\+\-]\-?\d+\.?\d*\^?\d*[a-z]\^?\d*",string)[0]
			input2 = re.findall("\-?\d+\.?\d*\^?\d*[a-z]\^?\d*[\+\-](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string)[0]
			#print(input1,input2)
			part = varAdd(input1,input2)
			string = string.replace(input1 + "+" + input2, str(part))
			print("b:")
		#if variables -
		if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\-](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string):
			input1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\+\-]\-?\d+\.?\d*\^?\d*[a-z]\^?\d*",string)[0]
			input2 = re.findall("\-?\d+\.?\d*\^?\d*[a-z]\^?\d*[\+\-](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string)[0]
			#print(input1,input2)
			part = varSub(input1,input2)
			string = string.replace(input1 + "-" + input2, str(part))
			break

	#return the new string
	return string

############################################################################################################################################################################################
#############################################################################################################################################################################################
#combining for order of oportations

#muliplication and division
def multiplicationDivision(string):


############################################################################################################################################################################################
#############################################################################################################################################################################################

def distrib(string):
	#print("Distributive Property:")
	#if something is multiplied with (...)
	if re.findall(TERM + "\(.+\)",string):
		#term multiplied with (...)
		outside = re.findall("(\-?\d*\.?\d*[a-z]*\^?\-?\d*\.?\d*[a-z]?)\(.+\)",string)[0]
		#piece inside the ()
		inside = re.findall("\((.+)\)",string)[0]
		#simplifiying the inside
		inside = multiplicationDivision(inside)
		#simplified terms of inside (spererated by + or -)
		terms = re.findall("[^\+\-]+",inside)
		#operators (+ or -) between terms
		operators = re.findall("[\+\-]+",inside)
		#answerterms array defined
		answerTerms = []
		#multiply terms with outside - multiply out
		for term in terms:
			#ans is = to the new multiplied out terms
			ans = multiplication(outside + "*" + str(term))
			#link all the new terms (ans) together
			answerTerms.append(ans)

		print("answer terms:")
		print(answerTerms)

		answerString = ""
		print("HEREEE")
		print(operators,answerTerms)
		if len(answerTerms) == len(operators) + 1:
			answerString = answerString + answerTerms[0]
			for i in range(0,len(operators)):
				answerString = answerString + operators[i] + answerTerms[i+1]
			print("answerString!:")
			print(answerString)
			####how do I make answersting print all look the smae and how do I make the code go to line 782 (next line of code following this one...?)
			answerString = summation(answerString)
			print("answerString final:")
			print(answerString)
			print("DONE!!!!")
			#####needs to be able to do it out of order (ex: 3x+2-2x+10 = 12+x)	
	return string


#############################################################################################################################################################################################
#############################################################################################################################################################################################
#calling on functions

print("welcome to calculator.py")

#inputs
debug = True

if debug:
	operation = '2^2*5'
else:
	operation = input("What calculation would you like to complete:")


#testing
#print(varMulComb("2","x"))
#print(multiplication("x*2*4x^2*2*4.5*-x*x"))
#print(sumNums("3x+4-9x+8-11+21y-3-5"))
#print(varMul("2x","4x^4"))
print(distrib("3x(9/3*2+2x-4)"))


########MAKE IT ALPHABETICAL right before spitting out the answer
