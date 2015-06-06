"""
Solution to the following problem:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1

"""

from numpy import floor, ceil

def series_sum(init, diff, num):
	return (init + (init + diff * (num-1))) * num / 2

# Inputs
THREASHOLD = 1000
m1 = 3
m2 = 5

# Solution
m1m2 = m1 * m2
num_m1 = floor((THREASHOLD-1)/m1)
num_m2 = floor((THREASHOLD-1)/m2)
num_m1m2 = floor((THREASHOLD-1)/m1m2)
solution = series_sum(m1, m1, num_m1) + series_sum(m2, m2, num_m2) - series_sum(m1m2, m1m2, num_m1m2)
print("The solution to this problem is:", solution)

