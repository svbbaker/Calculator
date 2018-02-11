#Simple Calulator
#Sophia Baker
#January/February 2018

#Regex
import re


#variables
#variable multiplicaiton
def varMult(input1,input2):
	print("Variable Multiplicaiton:")
	exp = 0
	coef = 1
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
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
	else: false

	return answer

#variable Addition
def varAdd(input1,input2):
	print("Variable Addition:")
	coef = 1
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
	exp1 = re.findall("\^(\-?\d+)",input1)[0]
	exp2 = re.findall("\^(\-?\d+)",input2)[0]
	print(exp1,exp2)
	if var1 == var2:# and if EXPONENTS ARE THE SAME:
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
		answer = a+b
	else: false
	
	return answer


#inputs
debug = True

if debug:
	operation = "x*x*x=16"
else:
	operation = input("What calculation would you like to complete:")

a = '4x^7'
b = '2x^-3'
print(varMult(a,b))
print(varAdd(a,b))

#REGEX
#distribution: \d*[a-z]*\(.+[\+\-].+\)
