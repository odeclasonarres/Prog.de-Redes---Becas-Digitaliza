from os import strerror
try:
	ccnt = lcnt = 0
	s = open('prueba.md','rt')
	line = s.readline()
	while line != '':
		lcnt += 1
		for ch in line:
			print(ch,end='')
			ccnt += 1
		line = s.readline()
	s.close()
	print("Characters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))
