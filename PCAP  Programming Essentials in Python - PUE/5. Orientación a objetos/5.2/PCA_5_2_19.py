class Stack:
	def __init__(self):
		self.__stk = []

	def push(self, val):
    		self.__stk.append(val)

	def pop(self):
    		val = self.__stk[-1]
    		del self.__stk[-1]
    		return val

class AddingStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.__sum = 0

	def getSum(self):
		return self.__sum

	def push(self, val):
		self.__sum += val
		Stack.push(self,val)

	def pop(self):
	 	val = Stack.pop(self)
	 	self.__sum -= val
	 	return val

stack = AddingStack()
for i in range(5):
	stack.push(i)
print(stack.getSum())
for i in range(5):
	print(stack.pop())