"""
Solution to the following problem:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3

"""

from numpy import sqrt

n = 600851475143
lpf = 1

if n % 2 == 0:
	lpf = 2
	while n % 2 == 0:
		n = n / 2

k = 3
ulimit = sqrt(n)
while n != 1 and k < ulimit:
	if n % k == 0:
		n = n / k
		lpf = k
	else:
		k = k + 2

