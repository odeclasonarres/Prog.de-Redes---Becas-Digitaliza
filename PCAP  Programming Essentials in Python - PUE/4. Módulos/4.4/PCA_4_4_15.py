try:
	x = int(input())
	y = 1 / x
	print(y)
except ValueError:
	print('You had to enter an integer value!')
except:
	print('Oh, dear!')
print('THE END')