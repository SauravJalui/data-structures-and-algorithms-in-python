from exceptions import Empty

class ArrayDeque:

	def __init__(self):
		self.data = []
		self.front = 0

	def __len__(self):
		return len(self.data)

	def is_empty(self):
		return len(self.data) == 0

	def first(self):
		if self.is_empty():
			raise Empty("Deque is Empty ")
		return self.data[self.front]

	def add_first(self, e):
		self.data.insert(self.front, e)

	def add_last(self, e):
		self.data.append(e)

	def delete_first(self):
		if self.is_empty():
			raise Empty("Deque is Empty ")
		value = self.data.pop(self.front)
		return value

	def delete_last(self):
		if self.is_empty():
			raise Empty("Deque is Empty ")
		return self.data.pop()
		


d = ArrayDeque()
d.add_last(10)
d.add_last(20)
d.add_last(30)
d.add_last(40)
d.add_last(50)
print("Deque:" , d.data)
print("delete_first:" , d.delete_first())
print("Deque:" , d.data)
print("delete_last:" , d.delete_last())
print("Deque:" , d.data)
d.add_first(50)
print("Deque:" , d.data)
d.add_last(60)
print("Deque:" , d.data)