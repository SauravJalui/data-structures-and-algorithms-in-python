from exceptions import Empty

class ArrayStack:
	def __init__(self):
		self.data = []

	def __len__(self):
		return len(self.data)

	def is_empty(self):
		return len(self.data) == 0

	def push(self , e):
		self.data.append(e)

	def pop(self):
		if self.is_empty():
			raise Empty("Exception")
		return self.data.pop()

	def top(self):
		if self.is_empty():
			raise Empty("Exception")
		return self.data[-1]

s = ArrayStack()
s.push(10)
s.push(20)
print ("Stack:", s.data)
print("Length:", len(s))
print("isempty:", s.is_empty())
print("Popped:", s.pop())
print ("Stack:", s.data)
print("Length:", len(s))
s.push(30)
s.push(40)
print("Top Element:", s.top())
print("Length:", len(s))

