"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6
"""

k = 100

def diff(n):
	assert n >= 1, "Invalid input, input value has to be a positive integer"
	if n == 1:
		return 0
	return 2 * n * (n * (n-1) / 2) + diff(n-1)

diff(k)