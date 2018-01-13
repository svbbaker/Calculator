print("welcome to calculator.py")

#returns the summ of two numbers
def add(num1,num2):
	return  num1 + num2

#returns the difference of two numbers
def subtract(num1,num2):
	return  num1 - num2

#returns the pruduct (*) of two numbers
def multiply(num1,num2):
	return  num1 * num2

#returns the product (/) of two numbers
def devide(num1,num2):
	return  num1 / num2

def multiplyArray(array): #mutiply the pieces in the array (take it as an int not as a sting)
	#for i in range(0,5):#between the numer or parts of the array
	result = 0
	result = multiply(int(array[0]),int(array[1])
	return result
def main():
	#If true, operation will not require input. If False, operation will require input
	debug = True

	if debug:
		operation = "5*2"
	else:
		operation = raw_input("What calculation would you like to complete:")

	if "*" in operation:
		split = operation.split("*")
		print(split)
		result = multiplyArray(split)

		answer = 1

		#for value in split:
			#answer = multiply(answer, int(value))

		#result = answer

	return result
	 
	#if (operation == "+") or (operation == "-") or (operation == "*") or (operation == "/"): # do the operation
		#num1 = input("enter the first number:")
		#num2 = input("enter the second  number:")
		#if(operation == "+"):
		#	print(add(num1,num2 ))
		#elif(operation == "-"):
		#	print(subtract(num1,num2 ))
		#elif(operation == "*"):
		#	print(multiply(num1,num2 ))
		#elif(operation == "/"):
		#	print(devide(num1,num2 ))
		#else:
		#	print("invalid input")
	#else: 
		#invalid operation
		#print("you must enter a valid operation")

main() 

