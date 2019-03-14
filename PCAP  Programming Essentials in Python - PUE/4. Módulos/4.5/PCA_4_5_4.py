try:
	y = 1 / 0
except ZeroDivisionError:
	print('Zero division!')
except ArithmeticError:
	print('Arithmetic problem!')
print('THE END')