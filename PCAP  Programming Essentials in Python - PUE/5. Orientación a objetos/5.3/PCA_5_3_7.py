class Class:
	Var = 1
	def __init__(self,val):
		Class.Var = val

print(Class.__dict__)
object = Class(2)
print(Class.__dict__)
print(object.__dict__)