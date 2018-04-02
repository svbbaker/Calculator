#Calulator
#Sophia Baker
#2018

#Regex
import re


#############################################################################################################################################################################################
#############################################################################################################################################################################################
#NUMBERS

#Multiplication and Division
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

#NOT DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:
#Addition and Subtraction
def sumAll(string):
	#print("Addition & Subtraction:")
	#if there is a + or - in the input string then run loop
	if '+' in string or '-' in string:
		#iterate throught the symbols in the string using i
		for i in string:
			#if i is equal to + or -
			if i == '+' in string or i == '-' in string:
				#finds the pieces around the sybol + or -
				line = re.findall("(\-?\d\.?\d*e\+\d+|\-?\(?\d+\.?\d*\)?)", string)
				#sum the piecies using a for loop
				answer = sum(float(x) for x in line)
				#break out of if 
				break
	#if there is no + or - sybol in input string:
	else:
		#keep the answer equal to the intial string
		answer = string

	#return the new string
	return answer

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
		answer = sumAll(answer)
		
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

			#############ADD IN PARENTHISIS INTO REGEX ABOVE (LOOK TO LAST SECTION IN CODE)!!!!!!!

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

			#############ADD IN PARENTHISIS INTO REGEX ABOVE (LOOK TO LAST SECTION IN CODE)!!!!!!!
			
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

	#if the variables are not equivalent
	else:
		#creating variables = strings that are variables	
		#a: input1 as string
		a = "%s" %input1
		#b: input2 as string
		b = "%s" %input2
		#anser: combined variables holding the variable parts as strings (a and b seperated by * symbol)
		answer = a + "*" + b

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
		a = "%s" %input1
		b = "%s" %input2
		answer = a + "*" + b

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
		a = "%s" %input1
		b = "%s" %input2
		answer = a + "-" + b

	return answer


#############################################################################################################################################################################################
#############################################################################################################################################################################################
#MIXED

###########ENCORPERATE PARENTHISIS:


#variable combined multiplicaiton
def varMulComb(input1,input2):
	#print("Variable Combined Multiplicaiton:")

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

	################!!!!!!!!!!!!!!!!!!!!!!! if variable in both: break !!!!!!!!!!!!!!!!!!!!!!!

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
		#exponents
		if re.findall("\^(\-?\d+)",variable):
			n = re.findall("\^(\-?\d+)",variable)[0]
			n = float(n)
			exp = exp + n 
		else: exp = 1
		#####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NEGATIVE EXPONENTS !!!!!!!!!!!!!!!!!!!!!
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
		answer = a + "/" + b

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

	#if g == False:
	#if they are not the same then there is a value for var and num
	#number of variable occerences
	exp = variable.count(var)
	#exponents
	if re.findall("\^(\-?\d+)",variable):
		n = re.findall("\^(\-?\d+)",variable)[0]
		n = float(n)
		if g == False:
			exp = (exp + n -1)*(-1) #-1 so that we dont acount for an extera variable from count above
		if h == False:
			exp = exp + n - 1
	if re.findall("(\d+\^[\-?\d+])",number):
		number = exponent(number)
	#coeffients
	if re.findall("(?<![\^\-])[\-\d\.]+",variable):
		n = re.findall("(?<![\^\-])[\-\d\.]+",variable)[0]
		n = float(n)
		coef = coef * n
	#divide the coeffient in the polynomial and the number, by: denpending on which one is variable1
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
	print("Exponents:")
	while len(re.findall("(\(?\d+\.?\d*\)?)\^(\(?\d+\.?\d*\)?)",string))>0:
		var1 = re.findall("(\(?\d+\.?\d*\)?)\^",string)[0]
		print(var1)
		var2 = re.findall("\^(\(?\d+\.?\d*\)?)",string)[0]
		print("exp = " + var2)
		answer = float(var1) ** float(var2)
		print("answer:")
		print(answer)
		string = string.replace(var1 + "^" + var2, str(answer))
		print(string)
	return string

###########ENCORPERATE PARENTHISIS:

#Multiplicaiton
def multiplication(string):
	while "*" in string:
		#if variables
		if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string):
			var1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*]",string)[0]
			var2 = re.findall("[\*](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varMul(varA,varB)
			string = string.replace(var1 + "*" + var2, str(part))
		#if variable and number
		if re.findall("(\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)[\*](\-?\d+\.?\d*\^?\d*)|(\-?\d+\.?\d*\^?\d*)[\*](\-?\d+\.?\d*\^?\d*[a-z]\^?\d*)",string):
			var1 = re.findall("(\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)[\*]",string)[0]
			var2 = re.findall("[\*](\-?\d+\.?\d*\^?\d*[a-z]?\^?\d*)",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varMulComb(varA,varB)
			string = string.replace(var1 + "*" + var2, str(part))
		#if numbers
		if re.findall("(\-?\d+\.?\d*\^?\d*)[\*](\-?\d+\.?\d*\^?\d*)",string):
			var1 = re.findall("(\-?\d+\.?\d*\^?\d*)[\*]",string)[0]
			var2 = re.findall("[\*](\-?\d+\.?\d*\^?\d*)",string)[0]
			varA = exponent(var1)
			varB = exponent(var2)
			part = varA + "*" + varB
			part = md(part)
			string = string.replace(var1 + "*" + var2, str(part))
	return(string)


#############################################################################################################################################################################################
#############################################################################################################################################################################################
 
def distrib(string):
	print("Distributive Property:")
	if re.findall("((\-?\d+\.?\d?\^?\(?.+\)?[a-z]?\^?\(?.+\)?|\-?[a-z]+\^?\(?.+\)?\d?\^?\(?.+\)?)\(.+\))",string):
		inside = re.findall("\((.+)\)",string)[0]
		#doenst work when extera parenth inside:
		#num = re.findall("[\+\-](\d?\^?\(?.+\)?[a-z]?\^?\(?.+\)?)\(.+\)",string)[0] ######HELPPPPPP
		######HELPPPPPP
		######HELPPPPPP
		num = re.findall("(\d+)\(.+\)",string)[0]
		#num = exponent(num)
		#nun = multiplication(num)
		#num = division(num)
		print("num: " + num)
		#PARENTHISIS
		#inside = parenthisis(inside)
		inside = multiplication(inside)
		print("string = " + inside)
		#split into + and - 
		var1 = re.findall("(\d+\.?\d?\^?\(?\-?\d?\.?\d?[a-z]?\)?[a-z]?\^?\(?\-?\d?\.?\d?[a-z]?\)?|\-?[a-z]+\^?\(?\-?\d?\.?\d?[a-z]?\)?\d?\.?\d?\^?\(?\-?\d?\.?\d?[a-z]?\)?)[\+\-]",inside)[0]
		var2 = re.findall("[\+\-](\d+\.?\d?\^?\(?\-?\d?\.?\d?[a-z]?\)?[a-z]?\^?\(?\-?\d?\.?\d?[a-z]?\)?|\-?[a-z]+\^?\(?\-?\d?\.?\d?[a-z]?\)?\d?\.?\d?\^?\(?\-?\d?\.?\d?[a-z]?\)?)",inside)[0]
		print("v1:" + var1)
		print("v2:" + var2)
		#creating new string to multiply in the coeficient before the inside (...)
		#####DID NOT WORK WITH OTHER FOR LOOP

		#sorting into array sothat num can be multipled to it
		#for i in range(0,len(var1)+len(var2)):
		#	m = "*"
		#	###WHAT DO I DO INSTEAD OF SOMETHING
		#	something = "+"
		#	newstring1 = num + m + var1[i]
		#	newstring2 = num + m + var2[i]
		#	newstring = 
		#	print(newstring)
		#print("newstring: "+newstring)
		
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
print(multiplication("3*2x^1"))


########MAKE IT ALPHABETICAL right before spitting out the answer



