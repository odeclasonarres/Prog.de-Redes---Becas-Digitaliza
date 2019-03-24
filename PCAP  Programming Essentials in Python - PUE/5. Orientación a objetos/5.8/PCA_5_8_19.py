try:
	stream = open("/home/odeclas/Documents/Cursos/Programación de Redes - Becas Digitaliza Cisco/PCAP  Programming Essentials in Python - PUE/5. Orientación a objetos/5.8/file.md","rt")
	# actual processing goes here
	stream.close()
except Exception as exc:
	print("open failed:", exc)
