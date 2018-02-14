#Simple Calulator
#Sophia Baker
#January/February 2018

#Regex
import re


#variables
#variable multiplicaiton
def varMul(input1,input2):
	print("Variable Multiplicaiton:")
	exp = 0
	coef = 1
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
	# -x replace eith -1x
	if var1 == var2:
		#num of variable occerences
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		exp = exp1 + exp2
		#if var1 in input1:
		#	exp += 1
		#if var2 in input2:
		#	exp += 1
		#exponents
		if re.findall("\^(\-?\d+)",input1):
			num = re.findall("\^(\-?\d+)",input1)[0]
			num = float(num)
			exp = exp + num -1 #-1 sothat we dont acount for an extera variable from count above
		if re.findall("\^(\-?\d+)",input2):
			num = re.findall("\^(\-?\d+)",input2)[0]
			num = float(num)
			exp = exp + num -1
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef * num #WHEN NO COEFF THEN MULTIPLIES EXP...
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp
		answer = a+b+c
	#####HOW DO YOU HANDEL -x WITHOUT A COEFF???
	else: 
		answer = False #"False"

	return answer

#variable Division
def varDiv(input1,input2):
	print("Variable Division:")
	exp = 0
	coef = 1
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
	if var1 == var2:
		#num of variable occerences
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		#exp = exp1 - exp2
		#exponents
		if re.findall("\^(\-?\d+)",input1):
			num = re.findall("\^(\-?\d+)",input1)[0]
			num = float(num)
			expA = exp1 + num -1 #-1 sothat we dont acount for an extera variable from count above
		if re.findall("\^(\-?\d+)",input2):
			num = re.findall("\^(\-?\d+)",input2)[0]
			num = float(num)
			expB = exp2 + num -1
		exp = expA - expB
		#coeffients
		if re.findall("(?<![\^\-])[\-\d\.]+",input1):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input1)[0]
			num = float(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		if re.findall("(?<![\^\-])[\-\d\.]+",input2):
			num = re.findall("(?<![\^\-])[\-\d\.]+",input2)[0]
			num = float(num)
			coef = coef / num #WHEN NO COEFF THEN MULTIPLIES EXP...
		a = "%s" %coef
		b = "%s" %var1
		c = "^%s" %exp
		answer = a+b+c
	#####HOW DO YOU HANDEL -x WITHOUT A COEFF???
	else: 
		answer = False #"False"
	return answer

#variable Addition
def varAdd(input1,input2):
	print("Variable Addition:")
	coef = 0
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
	exp1 = re.findall("\^(\-?\d+)",input1)[0]
	exp2 = re.findall("\^(\-?\d+)",input2)[0]
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
		answer = False #"False"

	return answer

#variable Addition
def varSub(input1,input2):
	print("Variable Subtraction:")
	coef = 0
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
	exp1 = re.findall("\^(\-?\d+)",input1)[0]
	exp2 = re.findall("\^(\-?\d+)",input2)[0]
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
		answer = False #"False"

	return answer


#inputs
a = '-x^2'
b = '2x^5'
print(varMul(a,b))
print(varDiv(a,b))
print(varAdd(a,b))
print(varSub(a,b))
