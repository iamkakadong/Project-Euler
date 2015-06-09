"""
Solution to the following problem:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4

"""

def isPalindrome(n):
	s = str(n)
	sr = s[::-1]
	return s == sr

i1 = 999
lp = 0

while i1 > 100:
	i2 = 999
	while i2 > 100:
		if i1 * i2 < lp:
			break
		if isPalindrome(i1 * i2):
			lp = i1 * i2
		i2 = i2 - 1
	i1 = i1 - 1
