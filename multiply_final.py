#!/usr/bin/env python3

#################################################################################
## NOTE:
##   The pympler python module is required to run this script.
##   Please install it by typing the following command in the terminal
##      pip3 install pympler
##
##   You may need sudo privileges depending on your installation
#################################################################################

import timeit, random

class Solution:
    def __init__(self, bits):
        self.bits = bits
        self.MAX_INT = int(pow(2, self.bits*2)//2)-1
        self.MIN_INT = int(pow(2, self.bits*2)//2)
        self.MASK = pow(2, bits*2)

    def generateRandomNum(self):
        return random.randrange(pow(-2, self.bits-1), pow(2, self.bits-1))

    def add(self, x, y):
        # Iterate till there is no carry
        while (y != 0):
            # carry now contains common
            # set bits of x and y
            carry = x & y
            #print("x:", x, "y:", y, "carry:", carry)

            # Exclusive OR
            # Sum of bits of x and y where at
            # least one of the bits is not set
            x = (x ^ y) % self.MASK

            # Carry is shifted by one so that   
            # adding it to x gives the required sum
            y = (carry << 1) % self.MASK

        return x if x <= self.MAX_INT else ~((x % self.MIN_INT) ^ self.MAX_INT) # to get rid of leading 1s for signed bit
        #If x > MAX_INT then take the mod of x with MIN_INT and xor with MAX_INT and negate to get the answer in x.

    def multiply(self, x,y):
        res = 0;
        while (y != 0):
            
            if (y & 1):
                res = self.add(res, x) # if y is odd, add x to result

            x = (x << 1) % self.MASK
            y = (y >> 1) % self.MASK
        return res
        
# We find the time and memory utilization for the test code. 
TEST_CODE = '''

for i, (num1, num2) in enumerate(zip(num1_list, num2_list)):
    result[i] = calc.multiply(num1, num2)
    #Answer check:
    if result[i] != (num1*num2):
        print("The multiplication of " + str(num1) + " and " + str(num2) + " is : " + str(result[i]), end=" ")
        print("FALSE!!!")

print("Bits:", bits, "\b, Size:", asizeof.asizeof(result), "bytes", end = ", ") 
'''

# setup code is not timed 
SETUP_CODE = '''

from __main__ import Solution

# To install library: pip3 install pympler
try:
    from pympler import asizeof # for memory utilization readings.
except ModuleNotFoundError:
    print("Please install the pympler module")
    print("Execute: 'pip3 install pympler'")
    exit()

bits = ***

calc = Solution(bits) # Calc is an object for the class Solution. 

# empty lists to store input values.
num1_list = []
num2_list = []

for i in range(1000):
    num1_list.append(calc.generateRandomNum())
    num2_list.append(calc.generateRandomNum())

# Create an array with all the values = 0 to store results 
result = [0 for x in range(1000)]

'''


# Add an extra check to make user has installed the necessary modules
try:
    from pympler import asizeof # for memory utilization readings.

    bitSizeArray = [4, 8, 16, 32, 64, 128, 256, 512, 1024]

    for j, bitSize in enumerate(bitSizeArray):
        time = timeit.timeit(setup=SETUP_CODE.replace("***", str(bitSize)), stmt=TEST_CODE, number=1)
        time = time * 1000 # convert time to milli seconds for easier readings.
        print("Time:", "%.4f" % time, "ms") # limiting to 4 decimal places for time.

except ModuleNotFoundError:
    print("Pympler module not found...")
    print("Execute: 'pip3 install pympler' in your terminal")
    print("You may need sudo privileges depending on your installation...\n")
    exit()


bitSizeArray = [4, 8, 16, 32, 64, 128, 256, 512, 1024]






