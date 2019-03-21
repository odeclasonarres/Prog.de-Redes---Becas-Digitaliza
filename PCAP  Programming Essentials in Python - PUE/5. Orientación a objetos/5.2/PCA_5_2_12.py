class Stack:
	def __init__(self):
		self.__stk = []

	def push(self, val):
    		self.__stk.append(val)

	def pop(self):
    		val = self.__stk[-1]
    		del self.__stk[-1]
    		return val

stack1 = Stack()
stack2 = Stack()
stack1.push(3)
stack2.push(stack1.pop())
print(stack2.pop())
