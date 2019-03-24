def PowersOf2(n):
	pow = 1
	for i in range(n):
		yield pow
		pow *= 2

for i in range(20):
	if i in PowersOf2(4):
		print(i)