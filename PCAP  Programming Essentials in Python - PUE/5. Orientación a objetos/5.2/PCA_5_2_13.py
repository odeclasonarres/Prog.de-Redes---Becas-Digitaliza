class Stack:
	def __init__(self):
		self.__stk = []

	def push(self, val):
    		self.__stk.append(val)

	def pop(self):
    		val = self.__stk[-1]
    		del self.__stk[-1]
    		return val

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()
little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)
print(funny_stack.pop())