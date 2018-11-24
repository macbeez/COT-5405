#################################################################################################################################################
# FINAL PROJECT SUBMISSION
# Course Name: COT 5405
# Date: 11/26/2018
# Group Number: 14
#################################################################################################################################################

Problem Definition: 

Perform LU Decomposition, Partial Pivot LU Decomposition and Complete Pivot LU Decomposition on 10 input matrices that are generated randomly.
Provide benchmarks such as Time taken for the execution and memory usage in each case. Also, show the correctness of the algorithm (source code).

#################################################################################################################################################

Formulas Used: 

a) LU Decomposition :=> A = LU
b) Partial Pivot LU Decomposition :=> PA = LU
c) Complete Pivot LU Decomposition :=> PAQ = LU

where where P and Q are permutation matrices,
A is the randomly generated square matrix of size 3 x 3 
L is the Lower Triangular matrix and U is the Upper Triangular matrix.

############################################################################################################################################

Language used to code the program: Python, version: 3.5 and MATLAB (For validating correctness only)
Operating system on which the code was executed: macOS Mojave, version: 10.14.1
Specifications of the system with which the code was executed: Intel Core i5 processor with 2.9GHz with 16 GB memory. 

############################################################################################################################################

Python libraries required:

1. Random
2. Fractions
3. Sys
4. Time
5. Numpy

############################################################################################################################################

Input:

Square matrix A of size 3 x 3, the elements of which are randomly generated.

#############################################################################################################################################

Output:

The output in all three cases are text files, that is, with A, L, U and Product (L * U) for LU decomposition 
P, A, L, U Product 1 (P * A) and Product 2 (L * U) for Partial Pivot LU Decomposition.
P, A, Q, L, U Product 1 (P * A * Q) and Product 2 (L * U) for Complete Pivot LU Decomposition.
It is noted that Product 1 and Product 2 are same for all the 10 iterations. Benchmarks such as time taken to 
execute the code and maximum memory used are also outputted.

#############################################################################################################################################


