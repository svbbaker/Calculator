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
	if 'x' in input1:
		exp += 1
	if 'x' in input2:
		exp += 1
	if re.findall("\d+",input1):
		num = re.findall("(\d+)",input1)
		coef = coef * num #make into floats
	if re.findall("\d+",input2):
		num = re.findall("(\d+)",input2)
		coef = coef * num
	answer = coef, exp
	return answer


#inputs
debug = True

if debug:
	operation = "x*x*x=16"
else:
	operation = input("What calculation would you like to complete:")

a = '2x'
b = '3x'
print(varMult(a,b))

#REGEX
#distribution: \d*[a-z]*\(.+[\+\-].+\)
