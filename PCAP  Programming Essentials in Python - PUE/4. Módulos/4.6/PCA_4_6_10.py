from math import exp
ex = 1
try:
	while True:
		print(exp(ex))
		ex *= 2
except OverflowError:
	print('Number is too big.')
