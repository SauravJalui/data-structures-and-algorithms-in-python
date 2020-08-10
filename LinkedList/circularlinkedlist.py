from exceptions import Empty

class CircularLinkedList:
	class Node:
		__slots__ = "element", "next"

		def __init__(self, element, next):
			self.element = element
			self.next = next

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def add_first(self, e):
		n1 = self.Node(e, None)
		if self.isEmpty():
			self.head = n1
			self.tail = n1	
			n1.next = n1
		else:
			self.tail.next = n1
			n1.next = self.head
		self.head = n1
		self.size += 1

	def add_last(self, e):
		n1 = self.Node(e, None)
		if self.isEmpty():
			self.head = n1
			self.tail = n1	
			n1.next = n1
		else:
			n1.next = self.tail.next
			self.tail.next = n1
		self.tail = n1
		self.size += 1

	def add_any(self, e, pos):
		n1 = self.Node(e, None)
		thead = self.head
		i = 1
		while i < pos - 1:
			thead = thead.next
			i += 1
		n1.next = thead.next
		thead.next = n1
		self.size +=1

	def remove_first(self):
		if self.isEmpty():
			raise Empty("List is empty")
		oldhead = self.tail.next
		self.tail.next = oldhead.next
		self.head = oldhead.next
		self.size -= 1
		if self.isEmpty():
			self.tail = None
		return oldhead.element
		
	def remove_last(self):
		if self.isEmpty():
			raise Empty("List is empty")
		thead = self.head
		i = 0
		while i < len(self) - 2:
			thead = thead.next
			i += 1
		self.tail = thead
		thead = thead.next
		self.tail.next = self.head
		value = thead.element
		self.size -= 1
		return value

	def remove_any(self, pos):
		if self.isEmpty():
			raise Empty("List is empty")
		thead = self.head
		i = 1
		while i < pos - 1:
			thead = thead.next
			i += 1
		value = thead.next.element
		thead.next = thead.next.next
		self.size -= 1
		return value

	def display(self):
		thead = self.head
		i = 0
		while i < len(self):
			print(thead.element, end = "-->")
			thead = thead.next
			i += 1
		print()

CL = CircularLinkedList()
CL.add_last(10)
CL.add_last(20)
CL.add_last(30)
CL.add_last(40)
CL.display()
print("Deleted: ", CL.remove_first())
CL.display()
CL.add_first(70)
CL.display()
print("Deleted: ", CL.remove_last())
CL.display()