def badfun(n):
	try:
		return 1/n
	except ArithmeticError:
		print('Sorry for the arithmetic!')
	return None

badfun(0)
print('THE END')