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

#Arrays call on caluculatons, to calulate mutliple variables:
def addArray(array):
	return add(int(array[0]),int(array[1]))

def subtractArray(array):
	return subtract(int(array[0]),int(array[1]))

def multiplyArray(array):
	#for i in range(0,5) #between the numer or parts of the array - NEEDS WORK
	return multiply(int(array[0]),int(array[1]))
#def multiplyArray(array): #mutiply the pieces in the array (take it as an int not as a sting)
	#for i in range(0,5):#between the numer or parts of the array
	#return multiply(int(array[0]),int(array[1])

def devideArray(array):
	return devide(int(array[0]),int(array[1]))


#main() calls on calculations
def main():

	#If true, operation will not require input. If False, operation will require input
	debug = True

	if debug:
		operation = "9*2"
	else:
		operation = input("What calculation would you like to complete:") #or raw_input ?


	if "+" in operation:
		split = operation.split("+")
		result = addArray(split)

		answer = 0

		for value in split:
			answer = add(answer, int(value))

		result = answer


	elif "-" in operation:
		split = operation.split("-")
		result = subtractArray(split)

		answer = 0

		for value in split:
			answer = subtract(result, int(value)) #if there are only two number subtracts the last number twice

		result = answer


	elif "*" in operation:
		split = operation.split("*")
		result = multiplyArray(split)

		answer = 1

		for value in split:
			answer = multiply(answer, int(value))

		result = answer


	elif "/" in operation:
		split = operation.split("/")
		result = devideArray(split)

		answer = 1

		for value in split:
			answer = devide(answer, int(value)) #does evything worng...

		result = answer


	else: resutl = "Error"

	#results of main()
	print(result)

	return result
	 
#Calling on funtion main()
main()

