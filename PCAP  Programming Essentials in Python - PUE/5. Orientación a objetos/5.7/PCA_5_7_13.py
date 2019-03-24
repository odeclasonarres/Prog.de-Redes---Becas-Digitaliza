list1 = []
for ex in range(6):
	list1.append(10 ** ex)
list2 = [10 ** ex for ex in range(6)]
print(list1)
print(list2)