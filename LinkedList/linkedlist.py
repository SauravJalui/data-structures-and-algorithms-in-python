
from exceptions import Empty

class LinkedList:	

	class Node:
		__slots__ = "element" , "next"

		def __init__(self, element, next):
			self.element = element
			self.next = next

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return (self.size)

	def is_empty(self):
		return self.size == 0

	def add_first(self, e):
		newest = self.Node(e, None)
		if self.is_empty():
			self.head = newest
			self.tail = newest
		else:
			newest.next = self.head
		self.head = newest
		self.size += 1

	def add_last(self, e):
		newest = self.Node(e , None)
		if self.is_empty():
			self.head = newest
			self.tail = newest
		else:
			self.tail.next = newest
		self.tail = newest
		self.size += 1

	def add_any(self, e, pos):
		newest = self.Node(e, None)
		thead = self.head
		i = 1
		while i < pos - 1:
			thead = thead.next
			i += 1
		newest.next = thead.next
		thead.next = newest
		self.size += 1

	def remove_first(self):
		if self.is_empty():
			raise Empty("Empty")
		value = self.head.element
		self.head = self.head.next
		self.size -= 1
		if self.is_empty():
			self.head = None
			self.tail = None
		return value

	def remove_last(self):
		if self.is_empty():
			raise Empty("Empty")
		thead = self.head
		i = 0
		while i < len(self) - 2:
			thead = thead.next
			i += 1
		self.tail = thead
		thead = thead.next
		value = thead.element
		self.tail.next = None
		self.size -= 1
		return value

	def remove_any(self, pos):
		if self.is_empty():
			raise Empty("Empty")
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
		while thead:
			print(thead.element, end = "-->")
			thead = thead.next
		print()
			
L = LinkedList()
L.add_last(10)
L.add_last(20)
L.add_last(30)
L.add_last(40)
L.display()
print("Deleted:", L.remove_first())
L.display()
L.add_first(70)
L.display()
print("Deleted:", L.remove_last())
L.display()
L.add_any(100, 2)
L.display()
L.remove_any(2)
L.display()
