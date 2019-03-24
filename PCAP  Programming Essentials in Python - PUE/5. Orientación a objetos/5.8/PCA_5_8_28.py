from os import strerror
try:
	stream = open("c:/users/user/Desktop/file.txt","rt")
	#stream = open("/home/odeclas/Documents/Cursos/Programación de Redes - Becas Digitaliza Cisco/PCAP  Programming Essentials in Python - PUE/5. Orientación a objetos/5.8/file.md","rt")

	# actual processing goes here
	stream.close()
except Exception as exc:
	print("File could not be opened:",strerror(exc.errno));
