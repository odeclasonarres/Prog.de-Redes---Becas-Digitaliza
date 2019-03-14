def badfun(n):
	raise ZeroDivisionError

try:
	badfun(0)
except ArithmeticError:
	print('What did you do?')
print('THE END')