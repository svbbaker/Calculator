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
		exp1 = input1.count(var1)
		exp2 = input2.count(var2)
		exp = exp1 + exp2
		#if var1 in input1:
		#	exp += 1
		#if var2 in input2:
		#	exp += 1
		if re.findall("\^(\-?\d+)",input1):
			num = re.findall("\^(\-?\d+)",input1)[0]
			num = int(num)
			print(num)
			exp = exp + num -1 #-1 sothat we dont acount for an extera variable from count above
		if re.findall("\^(\-?\d+)",input2):
			num = re.findall("\^(\-?\d+)",input2)[0]
			print(num)
			num = int(num)
			print(num)
			exp = exp + num -1
		if re.findall("\d+",input1):
			num = re.findall("(\d+)",input1)[0]
			num = int(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		if re.findall("\d+",input2):
			num = re.findall("(\d+)",input2)[0]
			num = int(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		answer = coef, var1, exp
	else: false

	return answer

#variable Addition
def varAdd(input1,input2):
	print("Variable Multiplicaiton:")
	exp = 0
	coef = 1
	var1 = re.findall("([a-z])",input1)[0]
	var2 = re.findall("([a-z])",input2)[0]
	if var1 == var2:
		if var1 in input1:
			exp += 1
		if var1 in input2:
			exp += 1
		if re.findall("\d+",input1):
			num = re.findall("(\d+)",input1)[0]
			num = int(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		if re.findall("\d+",input2):
			num = re.findall("(\d+)",input2)[0]
			num = int(num)
			coef = coef * num #WONT LET ME MULTIPLY FLOATS
		answer = coef, var1, exp
	else: answer = False
	return answer


#inputs
debug = True

if debug:
	operation = "x*x*x=16"
else:
	operation = input("What calculation would you like to complete:")

a = '4x^-2'
b = 'x^3'
print(varMult(a,b))

#REGEX
#distribution: \d*[a-z]*\(.+[\+\-].+\)
