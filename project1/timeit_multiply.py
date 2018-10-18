import timeit, random
from memory_profiler import memory_usage

class Solution:
    def __init__(self, bits):
        self.bits = bits
        self.MAX_INT = int(pow(2, self.bits*2)/2)-1
        self.MIN_INT = int(pow(2, self.bits*2)/2)
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
        
TEST_CODE = '''

num1 = calc.generateRandomNum()
num2 = calc.generateRandomNum()
result = calc.multiply(num1, num2)
#Answer check:
if result != (num1*num2):
    print("The multiplication of " + str(num1) + " and " + str(num2) + " is : " + str(result), end=" ")
    print("FALSE!!!")
'''

# setup code is not timed 
SETUP_CODE = '''

from __main__ import Solution
calc = Solution(bits = ***) #Calc is an object for the class Solution. 

'''

# bitSizeArray = [4, 8, 16, 32, 64, 128, 256, 512]


# for bitSize in bitSizeArray:
#     print(str(bitSize)+": ", timeit.timeit(setup=SETUP_CODE.replace("***", str(bitSize)), stmt=TEST_CODE, number=1000))

# print(timeit.timeit(setup=SETUP_CODE.replace("***", "16"), stmt=TEST_CODE, number=1000))

def mainApp():
    for i in range(1000):
        calc = Solution(bits = 8) #Calc is an object for the class Solution. 
        num1 = calc.generateRandomNum()
        num2 = calc.generateRandomNum()
        result = calc.multiply(num1, num2)
        #Answer check:
        if result != (num1*num2):
            print("The multiplication of " + str(num1) + " and " + str(num2) + " is : " + str(result), end=" ")
            print("FALSE!!!")


mem_usage = memory_usage(mainApp, interval=0.001)
# print('Memory usage (in chunks of 0.001 seconds): %s' % mem_usage)
print('Maximum memory usage: %s' % max(mem_usage))