print("welcome to calculator.py")

#returns the summ of two numbers
def add(num1,num2):
	return  var1 + var2

#returns the difference of two numbers
def subtract(num1,num2):
	return  var1 - var2

#returns the pruduct (*) of two numbers
def multiply(num1,num2):
	return  var1 * var2

#returns the product (/) of two numbers
def devide(num1,num2):
	return  var1 / var2


def main():
	#If true, operation will not require input. If False, operation will require input
	debug = True

	if debug:
		operation = "*"
	else:
		operation = raw_input("What calculation would you like to use? Please chose one (+,-,*,/):")

	 
	if (operation == "+") or (operation == "-") or (operation == "*") or (operation == "/"): # do the operation
		num1 = input("enter the first number:")
		num2 = input("enter the second  number:")
		if(operation == "+"):
			print(add(num1,num2 ))
		elif(operation == "-"):
			print(subtract(num1,num2 ))
		elif(operation == "*"):
			print(multiply(num1,num2 ))
		elif(operation == "/"):
			print(devide(num1,num2 ))
		else:
			print("invalid input")
	else: 
		#invalid operation
		print("you must enter a valid operation")
main() 

