def sortStack(s):
	if not s:
		return
	x = s.pop()
	sortStack(s)
	tempStack = []
	while s and s[-1] > x:
		tempStack.append(s.pop())
	s.append(x)
	while tempStack:
		s.append(tempStack.pop())

s = []
s.append(34)
s.append(3)
s.append(31)
s.append(98)
s.append(92)
s.append(23)

sortStack(s)
print("Sorted numbers are: ", end="")
while s:
	print(s.pop(), end=" ")
