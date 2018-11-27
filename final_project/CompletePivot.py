##################################################################################################################
# FINAL TEST - COMPLETE PIVOT LU DECOMPOSITION

# DESCRIPTION: This source code generates Complete Pivot LU Decomposition on 10 randomly generated matrices of 
# size 3 x 3. The formula used to perform the decomposition is PAQ = LU, where P and Q are permutation matrices,
# A is the randomly generated square matrix of size 3 x 3, L is the Lower Triangular matrix and U is the Upper
# Triangular matrix. The output is a text file, with P, A, Q, L, U, Product 1 (P * A * Q) and Product 2 (L * U).
# It is noted that Product 1 and Product 2 are same for all the 10 iterations. Benchmarks such as time taken to 
# execute the code and maximum memory used are also outputted.

##################################################################################################################

import random
import numpy as np
import fractions
import time
import sys 

A = []
L = []
U = []
P = []
Q = []
A1 = []
A2 = []
A3 = []
duration = [] # Holds the time taken for each iteration
memory = []

#Empty the file, each time you start execution
def clear_data_file(fileName):
    file = open(fileName, 'w')
    file.close()

def generate():
    global A, L, U, P, Q
    rows = 3
    cols = 3
    A = np.matrix(np.random.randint(1,100, size  = (rows, cols)))
    # A = np.matrix([[2,3,4], [4,7,5], [4,9,5]])
    L = np.zeros(shape=(3,3))
    L[0][0] = L[1][1] = L[2][2] = 1
    U = np.zeros(shape=(3,3))
    Pfinal = np.identity(3)
    Qfinal = np.identity(3)

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

clear_data_file("CompleteLUResults.txt")

print("\n\nBEGINNING OF LU DECOMPOSITION\n\n")

for n in range (0,10):
    generate()

    P1 = np.identity(3)
    Q1 = np.identity(3)
    np.set_printoptions(formatter={'all':lambda L: str(fractions.Fraction(L).limit_denominator())})

    start = time.time()
    # find the maximum value in the matrix
    i,j = np.unravel_index(A.argmax(), A.shape)

    # modify the permutation matrix
    tempP1 = P1[0].copy()
    P1[0], P1[i] = P1[i], tempP1
    tempQ1 = Q1[:,0].copy()
    Q1[:,0], Q1[:,j] = Q1[:,j], tempQ1

    PA1 = np.matmul(P1,A)
    PAQ1 = np.matmul(PA1, Q1)

    rowEchelon1(PAQ1)
    PAQ2 = A1
    rowEchelon2(PAQ2)
    P2 = np.identity(3)
    Q2 = np.identity(3)

    # To find the maximum value in the sub-matrix 2 x 2 and move it to (1,1) in matrix A2
    k = A2[1:3,1:3]
    i,j = np.where(k == (sorted(k.flatten().tolist())[-1]))
    i, j = i[0], j[0]
    if (i == 0 and j == 1):
        tempQ2 = Q2[:,1].copy()
        Q2[:,1], Q2[:,2] = Q2[:,2], tempQ2 
    elif (i == 1 and j == 0):
        tempP2 = P2[1].copy()
        P2[1], P2[i + 1] = P2[2], tempP2
        tempL = L[1,0].copy()
        L[1,0] = L[2,0]
        L[2,0] = tempL
    elif (i == 1 and j == 1):     
        tempP2 = P2[1].copy()
        tempQ2 = Q2[:,1].copy()
        P2[1], P2[i + 1] = P2[i + 1], tempP2
        Q2[:,1], Q2[:,j + 1] = Q2[:,j + 1], tempQ2
        tempL = L[1,0].copy()
        L[1,0] = L[2,0]
        L[2,0] = tempL
    else:
        pass

    PA2 = np.matmul(P2,A2)
    PAQ3 = np.matmul(PA2, Q2)
    rowEchelon3(PAQ3)

    U = A3

    Pfinal = np.matmul(P2,P1)
    Qfinal = np.matmul(Q1,Q2)

    PA = np.matmul(Pfinal, A)
    product1 = np.matmul(PA, Qfinal)
    product2 = np.matmul(L, U)

    # Get benchmarking data
    stop = time.time()
    memUsage = getCurrentMemUsage()
    duration.append(stop - start)
    memory.append(memUsage)

    print("\nRun ", n + 1)
    print("P:\n", Pfinal)
    print("A:\n", A)
    print("Q:\n", Qfinal)
    print("L:\n", L)
    print("U:\n", U)
    print("Product1:\n", product1)
    print("Product2:\n", product2)

    write_matrix_to_textfile("Run " + str(n+1) + ":\nA", A, "CompleteLUResults.txt")
    write_matrix_to_textfile("P", Pfinal, "CompleteLUResults.txt")
    write_matrix_to_textfile("Q", Qfinal, "CompleteLUResults.txt")
    write_matrix_to_textfile("L", L, "CompleteLUResults.txt")
    write_matrix_to_textfile("U", U, "CompleteLUResults.txt")
    write_matrix_to_textfile("Product of PAQ", product1, "CompleteLUResults.txt")
    write_matrix_to_textfile("Product of LU", product2, "CompleteLUResults.txt")

print("Total time taken for complete pivot LU decomposition of 10 matrices is: ", "{0:.6f}".format(sum(duration)), "seconds")
print("Maximum memory used for complete pivot LU decomposition of 10 matrices is: ", sum(memory), "bytes")


