import timeit
import random

def main():

	NumberOfInputs = int(input("Enter the number of inputs you want to test: "))
	bits = int(input("Enter the number of bits the input should have: "))

	def generateNumbers(bits, NumberOfInputs):
		numList = []
		for i in range(NumberOfInputs):
			#generate random number based on user input
			numList.append(random.randrange(pow(-2, bits-1), pow(2, bits-1))) #generate signed integer
		return numList

	def subtract(x, y):
		#If we are subtracting a larger number from a smaller number, the output is negated
		if x < y:
			x, y = y, x
			negate = True

		#Iterate till there is no carry:
		while (y != 0):
			#borrow will contain common set bits of y and unset bits of x
			borrow = (~x) & y
			#subtraction of bits of x and y where at least one of the bits is not set
			x = x ^ y
			#borrow is shifted by one so that subtracting it from x gives the required difference
			y = borrow << 1

		if 'negate' in vars() and negate == True: 
			#If it was negated in the beginning, we have to negate again to get the right answer
			negate = False
			return x * -1
		else:
			return x

	numList = generateNumbers(bits, NumberOfInputs)
	for index, num in enumerate(numList):
		if index % 2 == 0:
			x, y = numList[index], numList[index + 1]
			answer = subtract(x,y)
			print("The subtraction of " + str(x) + " and " + str(y) + " is : " + str(answer))
		#Answer check:
			if answer != (x-y):
				print("FALSE!!!")

main()