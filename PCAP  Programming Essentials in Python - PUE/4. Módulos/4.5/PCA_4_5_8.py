def badfun(n):
	return 1/n

try:
	badfun(0)
except ArithmeticError:
	print('What did you do?')
print('THE END')