class Left:
	Var = 'L'
	VarL = 'LL'
	def fun(self):
		return 'left'

class Right:
	Var = 'R'
	VarR = 'RR'
	def fun(self):
		return 'right'

class Sub(Left,Right):
	pass

object = Sub()

print(object.Var, object.VarL, object.VarR, object.fun())