from exceptions import Empty

class ArrayQueue:

	def __init__(self):
		self.data = []
		self.size = 0
		self.front = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0
 
	def enqueue(self, e):
		self.data.append(e)
		self.size += 1

	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		value = self.data[self.front]
		self.data[self.front] = None
		self.front += 1
		self.size -= 1
		return value

	def first(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		return self.data[self.front]

q = ArrayQueue()
q.enqueue(10)
q.enqueue(10)
print("Queue:", q.data)
print("Length:", len(q))
print("dequeue:", q.dequeue())
print("Queue:", q.data)
q.enqueue(30)
q.enqueue(40)
print("Queue:", q.data)
print("first element:", q.first())
print("Queue:", q.data)
print("dequeue:", q.dequeue())
print("first element:", q.first())
print("Queue:", q.data)