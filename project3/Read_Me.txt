##############################################################################################################################################
# PROGRAMMING ASSSIGNMENT - 3, Chapter: 4, Problem number: 4.
#
# Author: Monica Bernard
# Course Name: COT 5405
# Date: 11/20/2018
#############################################################################################################################################

Problem Definition: 

Some of your friends have gotten Into the burgeoning field of time-series data mining, in which one looks for patterns in sequences of events that occur over time. Purchases at stock exchanges--what’s being bought-- are one source of data with a natural ordering in time. Given a long sequence S of such events, your friends want an efficient way to detect certain "patterns" in them--for example, they may want to know if the four events:
						buy Yahoo, buy eBay, buy Yahoo, buy Oracle

occur in this sequence S, in order but not necessarily consecutively.
They begin with a collection of possible events (e.g., the possible’ transactions) and a sequence S of n of these events. A given event may occur multiple times in S (e.g., Yahoo stock may be bought many times In a single sequence S). We will say that a sequence S’ is a subsequence of S if there is a way to delete certain of the events from S so that the remaining events, in order, are equal to the sequence S’. So, for example, the sequence of four events above is a subsequence of the sequence

						buy Amazon, buy Yahoo, buy eBay, buy Yahoo, buy Yahoo, buy Oracle

Their goal is to be able to dream up short sequences and quickly detect whether they are subsequences of S. So this is the problem they
pose to you: Give an algorithm that takes two sequences of even~s--S’ of length m and S of length n, each possibly containing an event more than once--and decides in time O(m + n) whether S’ is a subsequence of S.

############################################################################################################################################

Goal of this program: This program checks to see if set S' (of size m) is a subset of set S (of size n) 

############################################################################################################################################

Language used to code the program: Python, version: 3.5
Operating system on which the code was executed: macOS Mojave, version: 10.14.1
Specifications of the system with which the code was executed: Intel Core i5 processor with 2.9GHz with 16 GB memory. 

############################################################################################################################################

Python libraries required:

1. Random
2. Secrets
3. Itertools
4. Time
5. Numpy
6. Matplotlib

############################################################################################################################################

Input:

A list of companies is provided in the program. Using this list, sets S (original set), S_opt (obtained by eliminating consecutive repitition of companies in S) and S_prime (the subset which we are searching for in S_opt) are randomly generated each time. The size of S is 
given by n where n = 1,2,3,...... 1000 and the size of subset S_prime is given by m where 
m = 1 for n = 1,2
m = 2 for n = 3
m = 3 for n = 4 to 1000

Intial tests were done by taking m = 5. But it was noticed that almost 99% of the times, it turned out that S_prime is not a subset of S_opt. 
Hence, for later executions m was taken as 3, where at least some subsets were noticed. 

#############################################################################################################################################

Output:

The outputs of the program are two text files. One of them contains the results for the brute force solution when n = 1,2,3,....10 and the other text file contains the results for the optimized solution when n = 1,2,3,.....1000. Also, two graphs are produced, one for the brute force solution and the other for the optimized solution. Each of these show n values along the x-axis and the time taken to search for a subset along the y-axis. 

#############################################################################################################################################


