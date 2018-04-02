import re

#Addition and Subtraction
def sumAll(string):
	#print("Addition & Subtraction:")
	#if there is a + or - in the input string then run loop
	while '+' in string or '-' in string:
		#iterate throught the symbols in the string using i
		#for i in string:
			#if i is equal to + or -
			#if i == '+' in string or i == '-' in string:
		#finds the pieces around the sybol + or -
		line = re.findall("([\+\-]?\-?\(?\d+\.?\d*\)?|)([\+\-]\-?\(?\d+\.?\d*\)?)", string)[0] ###ENCORPERATE E: (\-?\d\.?\d*e\+\d+|\-?\(?\d+\.?\d*\)?)
		#sum the piecies using a for loop
		print(line)
			# l = "6","7"
			# print("test:")
			# print(l)
			# print(sum(float(x) for x in l))
		answer = sum(float(x) for x in line) #for converts to float
		print(answer)
		#break out of if 
		#break
	#if there is no + or - sybol in input string:
	else:
		#keep the answer equal to the intial string
		answer = string

	#return the new string
	return answer


print(sumAll("3+4*4-3+5"))