try:
	x = int(input())
	y = 1 / x
	print(y)
except ZeroDivisionError:
	print('Cannot divide by zero – sorry!')
except ValueError:
	print('You have to enter an integer value!')
except:
	print('Oh, dear!')
print('THE END')