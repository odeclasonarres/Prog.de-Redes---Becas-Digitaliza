try:
	y = 1 / 0
except ArithmeticError:
	print('Arithmetic problem!')
except ZeroDivisionError:
	print('Zero division!')
print('THE END')