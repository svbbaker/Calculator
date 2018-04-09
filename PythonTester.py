import re

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

print(distrib("3x(1+2x)"))

