"""
Solution to the following problem:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5

"""

from numpy import sqrt, floor

k = 20
n = 1

while k > 1:
	tmp = sqrt(k)
	if floor(tmp) == tmp and n % k != 0:
		n = n * k
	k = k - 1

while k <= 20:
	if n % k != 0:
		n = n * k
	k = k + 1