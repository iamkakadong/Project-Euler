"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7
"""

from numpy import sqrt

k = 10001

def genPrime(n):
	L = [2]
	s = 3
	i = 1
	while i < n:
		isPrime = True
		tmp = sqrt(s)
		j = 0
		while L[j] < tmp:
			if s % L[j] == 0:
				isPrime = False
				break
			j = j + 1
		if isPrime:
			L.append(s)
			i = i + 1
		s = s + 2
	return s, L

(s,L) = genPrime(k)