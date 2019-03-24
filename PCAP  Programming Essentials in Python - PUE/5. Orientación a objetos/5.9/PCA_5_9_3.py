from os import strerror
try:
	cnt = 0
	s = open('prueba.md','rt')
	content = s.read()
	for ch in content:
		print(ch,end='')
		cnt += 1
	s.close()
	print("Characters in file:", cnt)
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))
