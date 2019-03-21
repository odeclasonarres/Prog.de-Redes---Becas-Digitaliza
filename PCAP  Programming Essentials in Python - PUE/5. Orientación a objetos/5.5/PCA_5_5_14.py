class Super:
	def __init__(self):
		self.supvar = 11

class Sub(Super):
	def __init__(self):
		super().__init__()
		self.subvar = 12

object = Sub()
print(object.subvar)
print(object.supvar)