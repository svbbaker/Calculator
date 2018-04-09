import re

#Addition and Subtraction
def sumAll(string):
	#print("Addition & Subtraction:")
	#while there is a + or - in the input string then run loop
	param = re.findall("(\+?\-?\d\.?\d*e\+\d+|\+?\-?\(?\d+\.?\d*\)?)([\+\-])(\+?\-?\d\.?\d*e\+\d+|\+?\-?\(?\d+\.?\d*\)?)", string)

	while len(param) > 0:
 
		#finds the pieces around the sybol + or -
		line = param[0]
		print(line)
		#sum the piecies using a for loop
		answer = float(line[0]) + float(line[1]+line[2]) #for converts to float
		print(string)
		print(answer)
		#replace the part (pieces of line) in input string with the answer from the operation
		string = string.replace(str(line[0]) + str(line[1]) + str(line[2]), str(answer))

		param = re.findall("(\+?\-?\d\.?\d*e\+\d+|\+?\-?\(?\d+\.?\d*\)?)([\+\-])(\+?\-?\d\.?\d*e\+\d+|\+?\-?\(?\d+\.?\d*\)?)", string)
	#return the new string
	return string


print(sumAll("5-17+21-78"))

