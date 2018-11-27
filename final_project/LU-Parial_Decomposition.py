########################################################################################################################################
# MID-TERM TESTING - LU DECOMPOSITION AND PARTIAL PIVOT LU DECOMPOSITION

# DESCRIPTION: This source code generates LU decomposition and Partial Pivot LU Decomposition on 10 randomly generated matrices of 
# size 3 x 3. The formula used to perform the LU decomposition is A = LU, and the formula use to perform partial pivot LU
# decomposition is PA = LU, where P is the permutation matrix, A is the randomly generated square matrix of size 3 x 3,
# L is the Lower Triangular matrix and U is the Upper Triangular matrix. The output in both cases are text files, with A, L, U
# and Product (L * U) for LU decomposition and P, A, L, U Product 1 (P * A) and Product 2 (L * U) for Partial Pivot LU Decomposition.
# It is noted that Product 1 and Product 2 are same for all the 10 iterations. Benchmarks such as time taken to 
# execute the code and maximum memory used are also outputted.

########################################################################################################################################

import random
import numpy as np
import fractions
import time
import sys

A = []
L = []
U = []
P = []
A1 = []
A2 = []
A3 = []
durationLU = [] # Holds the time taken for each iteration of LU decomposition
durationPartialLU = [] # Holds the time taken for each iteration of partial LU decomposition
memoryLU = []
memoryPartialLU = []

#Empty the file, each time you start execution
def clear_data_file(fileName):
    file = open(fileName, 'w')
    file.close()

def generate():
    global A, L, U
    rows = 3
    cols = 3
    A = np.matrix(np.random.randint(1,100, size  = (rows, cols)))
    # A = scipy.array([[2,4,-4], [1,-4,3], [-6,-9,5]])
    L = A1 = np.zeros(shape=(3,3))
    L[0][0] = L[1][1] = L[2][2] = 1
    U = A1 = np.zeros(shape=(3,3))

def write_matrix_to_textfile(label, a_matrix, txt_file):

    def compile_row_string(a_row):
        return str(a_row)

    with open(txt_file, 'a') as f:
        f.write(label + ":\n")
        for row in a_matrix:
            f.write(compile_row_string(row)+'\n')
        f.write("\n\n")
    return True

def rowEchelon1(X):
    global A, A1, L
    # Create empty matrix
    A1 = np.zeros(shape=(3,3))

    for i in range (0,3):
        coeff1 = (-1 * X[1,0]) / X[0,0]

        A1[0,i] = X[0,i] 
        A1[1,i] = (X[0,i] * (coeff1)) + X[1,i]
        A1[2,i] = X[2,i]

    # print("A1:\n", A1)
    # print("\nCoeff1: ", coeff1)
    L[1,0] = -1 * coeff1
    # print("L: ", L)

def rowEchelon2(X1):
    global A1, A2, L
    A2 = np.zeros(shape = (3,3))

    for i in range (0,3):
        coeff2 = (-1 * X1[2,0]) / X1[0,0]

        A2[0,i] = X1[0,i]
        A2[1,i] = X1[1,i]
        A2[2,i] = (X1[0,i] * (coeff2)) + X1[2,i]

    # print("A2:\n", A2)
    # print("\nCoeff2: ", coeff2)
    L[2,0] = -1 * coeff2

def rowEchelon3(X2):
    global A2, A3, L
    A3 = np.zeros(shape = (3,3))

    for i in range (0,3):
        coeff3 = (-1 * X2[2,1]) / X2[1,1]

        A3[0,i] = X2[0,i]
        A3[1,i] = X2[1,i]
        A3[2,i] = X2[1,i] * (coeff3) + X2[2,i]

    # print("A3:\n", A3)
    # print("\nCoeff3: ", coeff3)
    L[2,1] = -1 * coeff3

def getCurrentMemUsage():
    memory_sum = 0
    for object in globals():
        memory_sum += sys.getsizeof(object)
    return memory_sum

clear_data_file("LUResults.txt")
print("\n\nBEGINNING OF LU DECOMPOSITION\n\n")

for n in range (0,10):
    generate()
    print("\n\nRun ", n+1, ". Initial matrices A, L and U:\n")
    print("A:\n", A)
    print("L:\n", L)
    print("U:\n", U)

    start = time.time()
    rowEchelon1(A)
    rowEchelon2(A1)
    rowEchelon3(A2)
    
    stop = time.time()
    memUsage = getCurrentMemUsage()
    memoryLU.append(memUsage)
    durationLU.append(stop - start)

    write_matrix_to_textfile("Run " + str(n+1) + ":\nA", A, "PartialLUResults.txt")

    print("\n\nRun ", n+1, ". Final matrices L, U and Product\n")
    np.set_printoptions(formatter={'all':lambda L: str(fractions.Fraction(L).limit_denominator())})
    print("L:\n", L)
    write_matrix_to_textfile("L", L, "LUResults.txt")

    U = A3
    np.set_printoptions(formatter={'all':lambda U: str(fractions.Fraction(U).limit_denominator())})
    write_matrix_to_textfile("U", U, "LUResults.txt")
    print("U:\n", U)

    product = np.matmul(L,U)
    write_matrix_to_textfile("Product", product, "LUResults.txt")
    print("Product:\n",product)

print("\n\nEND OF LU DECOMPOSITION\n\n")

print("\n\nBEGINNING OF PARTIALLY PIVOTED LU DECOMPOSITION\n\n")

clear_data_file("PartialLUResults.txt")

for i in range (0,10):
    P =np.identity(3)
    generate()
    # A = np.matrix([[2,1,5], [4,4,-4], [1,3,1]])
    # A = np.matrix([ [47,60,33], [82,36,6], [15,40,26]])
    start = time.time()

    mat = np.matrix(A)
    col = 0
    col_list = [x[0] for x in mat[:,col].tolist()]
    max_num = max(col_list)
    max_index = col_list.index(max_num)

    #swapping permutation matrix, P
    temp = P[0].copy()
    P[0], P[max_index] = P[max_index], temp

    PA1 = np.matmul(P,A)
    rowEchelon1(PA1)

    PA2 = A1
    rowEchelon2(PA2)

    if A2[2,1] > A2[1,1]:
        P1 =np.identity(3)
        temp = P1[1].copy()
        tempP = P[1].copy()
        P1[1], P1[2] = P1[2], temp
        P[1], P[2] = P[2], tempP
        tempL = L[1,0].copy()
        L[1,0] = L[2,0]
        L[2,0] = tempL
        PA3 = np.matmul(P1,A2)
        rowEchelon3(PA3)
    else:
        PA3 = A2
        rowEchelon3(PA3)

    U = A3
    product1 = np.matmul(P, A)
    product2 = np.matmul(L, U)
    
    # Get benchmarking data
    stop = time.time()
    memUsage = getCurrentMemUsage()
    memoryPartialLU.append(memUsage)
    durationPartialLU.append(stop - start)

    print("\nRun ", i + 1)
    print("P:\n", P)
    print("A:\n", A)
    print("L:\n", L)
    print("U:\n", U)
    print("\nProduct of PA: \n", product1)
    print("\nProduct of LU: \n", product2)

    write_matrix_to_textfile("Run " + str(i+1) + ":\nA", A, "PartialLUResults.txt")

    np.set_printoptions(formatter={'all':lambda L: str(fractions.Fraction(L).limit_denominator())})
    write_matrix_to_textfile("L", L, "PartialLUResults.txt")

    np.set_printoptions(formatter={'all':lambda U: str(fractions.Fraction(U).limit_denominator())})
    write_matrix_to_textfile("U", U, "PartialLUResults.txt")

    write_matrix_to_textfile("Product of PA", product1, "PartialLUResults.txt")

    write_matrix_to_textfile("Product of LU", product2, "PartialLUResults.txt")

print("Total time taken for LU decomposition of 10 matrices is: ", "{0:.6f}".format(sum(durationLU)), "seconds")
print("Total time taken for Partial pivot LU decomposition of 10 matrices is: ", "{0:.6f}".format(sum(durationPartialLU)), "seconds")
print("Maximum memory used for LU decomposition of 10 matrices is: ", sum(memoryLU), "bytes")
print("Maximum memory used for Partial pivot LU decomposition of 10 matrices is: ", sum(memoryPartialLU), "bytes")












