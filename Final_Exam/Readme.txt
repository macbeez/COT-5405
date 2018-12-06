######################################################################################################################################################################################
# FINAL EXAM 
#
# Author: Monica Bernard
# Course Name: COT 5405
# Date: 12/07/2018
#
#
# Using the source code that convert a truth table to simplified Boolean expression using Quine-McCluskey Method.
#
# Written By: JongHewk Park 
# Last Edit : June 2, 2015
#
# Modified by: Monica Bernard 
# Last Edit: December 5, 2018
# Modification: Make script work in Python 3 and work as a library
######################################################################################################################################################################################

Problem Definition: 

Question 1:

Given a circuit, compute the truth table of the Boolean formula it implements. Run your code on the 5 input files provided to you; document your pseudocode and experimental results in a report. If you used any algorithms or results taught in the class, highlight them in your report.

Question 2:

The citizens of the land of Far Far Away have sought your help in designing network of resistances from Boolean formula. Write a program that reads a truth table and produces the network of resistances to implement the desired formula. Run your code on 5 benchmark files provided to you; document your pseudocode and experimental results in a report. If you used any algorithms or results taught in the class, highlight them in your report.
######################################################################################################################################################################################

Goal of this program: 

To check if the effective resistance of the circuit between nodes 0 and 1 is high or low. And, to build a circuit with resistors based on the truth table. 

######################################################################################################################################################################################

Language used to code the program: Python, version: 3.5
Operating system on which the code was executed: macOS Mojave, version: 10.14.1
Specifications of the system with which the code was executed: Intel Core i5 processor with 2.9GHz with 16 GB memory. 

######################################################################################################################################################################################

Python libraries required:

1. Tabulate
2. Sys
3. Itertools
4. Networkx
5. Numpy
6. Re

######################################################################################################################################################################################

Input:

For question 1, text files describing the resistor connections between different nodes in a circuit. For question 2, text files describing 
all the combinations of either high resistance or low resistance for all the resistors in the circuit.

######################################################################################################################################################################################
Output:

Final_Exam_Q1.py outputs the truth table showing the effective resistance in the circuit between nodes 0 to 1. A '0' in the output truth table
shows an effective low resistance in the circuit and a '1'in the output truth table shows an effective high resistance in the circuit. The program
also outputs a text file with the final result. 

Final_Exam_02.py outputs a circuit showing all the nodes between 0 and 1 and the corresponding resistors between these nodes. The program also outputs 
this result in a text file. 

######################################################################################################################################################################################


