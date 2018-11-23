################################################################################################################################
# PROGRAMMING ASSSIGNMENT - 3, Chapter: 4, Problem number: 4.
#
# Author: Monica Bernard
# Course Name: COT 5405
# Date: 11/20/2018
# Description: This program checks to see if set S' (of size m) is a subset of set S (of size n)
# Input: A list of companies from which we generate a random set (of size n = 1,2,3,....1000) each time
# Output: Two graphs (one for Brute Force and other for Optimized) each showing the amount of time taken
#		  to find the subset S' in S (for different n values). Two text files (one for Brute Force and other for Optimized)
#		  showing S, S_prime and S_opt (S without repetition) for different n values. 
###############################################################################################################################

import random
import secrets 
from itertools import groupby
import time
import matplotlib.pyplot as plt
import numpy as np

list_of_comp = ["Buy Amazon", "Buy Google", "Buy Microsoft", "Buy Yahoo", "Buy Apple", "Buy Oracle", "Buy eBay",
				"Buy Facebook", "Buy Instagram", "Buy Reddit"]
# n = int(input("Enter the size of S: "))
# m = int(input("Enter the size of S': "))

# define as global
S = []
S_prime = []
S_opt = []
n = 0
m = 0
duration = []
duration_BruteForce = []

def generate(n, m):
	# global S
	# global S_prime
	# global S_opt
	S = [secrets.choice(list_of_comp) for x in range (n)]
	# print(S, "\n")
	S_prime = random.sample(list_of_comp, m) # m < n and m < len(list_of_comp)
	# print(S_prime, "\n")
	S_opt = [x[0] for x in groupby(S)] # remove duplicates
	# print(S_opt, "\n")
	return [S, S_opt, S_prime]

# Brute Force Search
def BruteForce(S_opt, S_prime, m):
	start = time.time()
	for i in range(len(S_opt)):
		if S_opt[i : i + m] == S_prime:
			stop = time.time()
			duration_BruteForce.append(stop - start)
			return True
			break
		stop = time.time()
	stop = time.time()
	duration_BruteForce.append(stop - start) 
	return False

# Optimized code:
def Optimized(S_opt, S_prime, m):
	start = time.time()
	searchElement = ""
	searchElement = S_prime[0]
	# print(searchElement)
	searchList = [i for i,x in enumerate(S_opt) if x == searchElement]
	# print(searchList)
	if len(searchList) == 1:
		j = searchList[0]
		if S_opt[j : j + m] == S_prime:
			stop = time.time()
			duration.append(stop - start)
			return True	
	else:
		for i in range(len(searchList) - 1):
			if (abs(searchList[i+1] - searchList[i]) >= m):
				j = searchList[i]
				if S_opt[j : j + m] == S_prime: # may have to do j + m + 1, check it
					stop = time.time()
					duration.append(stop - start)
					return True
					break

	stop = time.time()
	duration.append(stop - start)
	return False

def fileWrite_BF(n, S, S_opt, S_prime, result):
	if n != 0:
		f1 = open("BruteForce_results.txt", "a")
		f1.write("n:"+str(n))
		f1.write("\n")
		f1.write("S:       ")
		for i,x in enumerate(S):
			f1.write(str(x))
			if (i != len(S)-1):
				f1.write(", ")
		f1.write("\n")
		f1.write("S_opt:   ")
		for i,x in enumerate(S_opt):
			f1.write(str(x))
			if (i != len(S_opt)-1):
				f1.write(", ")
		f1.write("\n")
		f1.write("S_prime: ")
		for i,x in enumerate(S_prime):
			f1.write(str(x))
			if (i != len(S_prime)-1):
				f1.write(", ")
		f1.write("\n\n")
		f1.write("Is S' a subset of S_opt?: " + str(result))
		f1.write("\n\n")
		f1.close()
	else:
		f1 = open("BruteForce.txt", "w")
		f1.close()

def fileWrite_Optimized(n, S, S_opt, S_prime, result):
	if n != 0:
		f2 = open("Optimized_results.txt", "a")
		f2.write("n:"+str(n))
		f2.write("\n")
		f2.write("S:       ")
		for i,x in enumerate(S):
			f2.write(str(x))
			if (i != len(S)-1):
				f2.write(", ")
		f2.write("\n")
		f2.write("S_opt:   ")
		for i,x in enumerate(S_opt):
			f2.write(str(x))
			if (i != len(S_opt)-1):
				f2.write(", ")
		f2.write("\n")
		f2.write("S_prime: ")
		for i,x in enumerate(S_prime):
			f2.write(str(x))
			if (i != len(S_prime)-1):
				f2.write(", ")
		f2.write("\n\n")
		f2.write("Is S' a subset of S_opt?:" + str(result))
		f2.write("\n\n")
		f2.close()
	else:
		f2 = open("Optimized.txt", "w")
		f2.close()

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

print("Clear datafile...")
fileWrite_BF(0, None, None, None, None)

print("Clear datafile...")
fileWrite_Optimized(0, None, None, None, None)

print("For n from 1 to 10, both BRUTE FORCE SOLUTION AND OPTIMIZED SOLUTION is provided \n \n")
n = 1
m = 1
S, S_opt, S_prime = generate(n,m)
result = BruteForce(S_opt, S_prime, m)
fileWrite_BF(n, S, S_opt, S_prime, result)
if (result):
	print("n: ", n, "Using Brute Force method, S_prime is a subset of S\n")
else:
	print("n: ", n, "Using Brute Force method, S_prime is NOT a subset of S\n")

for n in range (2,4):
	m = n - 1
	S, S_opt, S_prime = generate(n,m) 
	result = BruteForce(S_opt, S_prime, m)
	fileWrite_BF(n, S, S_opt, S_prime, result)
	if (result):
		print("n: ", n, "Using Brute Force method, S_prime is a subset of S\n")
	else:
		print("n: ", n, "Using Brute Force method, S_prime is NOT a subset of S\n")
		

for n in range (4,11):
	m = 3
	S, S_opt, S_prime = generate(n,m)
	result = BruteForce(S_opt, S_prime, m)
	fileWrite_BF(n, S, S_opt, S_prime, result)
	if (result):
		print("n: ", n, "Using Brute Force method, S_prime is a subset of S\n")
	else:
		print("n: ", n, "Using Brute Force method, S_prime is NOT a subset of S\n")

print("End of BRUTE FORCE SOLUTIONS \n \n")
print("Start of OPTIMIZED SOLUTIONS \n \n")

n = 1
m = 1
S, S_opt, S_prime = generate(n,m)
result_Op = Optimized(S_opt, S_prime, m)
fileWrite_Optimized(n, S, S_opt, S_prime, result_Op)
if (result_Op):
	print("n: ", n, "Using optimized method, S_prime is a subset of S\n")
else:
	print("n: ", n, "Using optimized method, S_prime is NOT a subset of S\n")


for n in range (2,4):
	m = n - 1
	S, S_opt, S_prime = generate(n,m)
	result_Op = Optimized(S_opt, S_prime, m)
	fileWrite_Optimized(n, S, S_opt, S_prime, result_Op)
	if (result_Op):
		print("n: ", n, "Using optimized method, S_prime is a subset of S\n")
	else:
		print("n: ", n, "Using optimized method, S_prime is NOT a subset of S\n")

for n in range (4,11):
	m = 3
	S, S_opt, S_prime = generate(n,m)
	result_Op = Optimized(S_opt, S_prime, m)
	fileWrite_Optimized(n, S, S_opt, S_prime, result_Op)
	if (result_Op):
		print("n: ", n, "Using optimized method, S_prime is a subset of S\n")
	else:
		print("n: ", n, "Using optimized method, S_prime is NOT a subset of S\n")

for n in range (11,1001):
	m = 3
	S, S_opt, S_prime = generate(n,m)
	result_Op = Optimized(S_opt, S_prime, m)
	fileWrite_Optimized(n, S, S_opt, S_prime, result_Op)
	if (result_Op):
		print("n: ", n, "Using optimized method, S_prime is a subset of S\n")
	else:
		print("n: ", n, "Using optimized method, S_prime is NOT a subset of S\n") 


fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
n_list = []
for i in range (1,1001):
	n_list.append(i)
ax1.plot(n_list, duration, 'r-', label = "raw data") 
ax1.plot(n_list, smooth(duration, 10), 'g-', label = "smooth data") 
ax1.set_title("Optimized Solution: Size of set S vs. Searching time of subset S' in S")
ax1.set_xlabel('Size of set S (n)')
ax1.set_ylabel('Time (ms)')
ax1.legend(loc = 'upper left')
ax1.grid(True)
plt.show()

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
n_list = []
for i in range (1,11):
	n_list.append(i)
ax2.plot(n_list, duration_BruteForce, 'r-', label = "raw data") 
# ax2.plot(n_list, smooth(duration_BruteForce, 10), 'g-', label = "smooth data") 
ax2.set_title("Optimized Solution: Size of set S vs. Searching time of subset S' in S")
ax2.set_xlabel('Size of set S (n)')
ax2.set_ylabel('Time (ms)')
ax2.legend(loc = 'upper right')
ax2.grid(True)
plt.show()