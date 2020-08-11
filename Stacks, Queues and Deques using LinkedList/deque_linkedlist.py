from exceptions import Empty

class LinkedQueue:
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

    def is_Empty(self):
        return self.size == 0
    
    def add_first(self, e):
        n1 = self.Node(e, None)
        if self.is_Empty():
            self.head = n1
            self.tail = n1
        else:
            n1.next = self.head
        self.head = n1
        self.size += 1    

    def add_last(self, e):
        n1 = self.Node(e, None)
        if self.is_Empty():
            self.head = n1
            self.tail = n1
        else:
            self.tail.next = n1
        self.tail = n1
        self.size += 1

    def remove_first(self):
        if self.is_Empty():
            raise Empty("deque is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_Empty():
            self.head = None
            self.tail = None
        return value
    
    def remove_last(self):
        if self.is_Empty():
            raise Empty("deque is empty")
        thead = self.head
        i = 0
        while i < len (self) - 2:
            thead = thead.next
            i += 1
        self.tail =thead
        thead = thead.next
        value = thead.element
        self.tail.next = None
        self.size -= 1
        return value
    
    def display(self):
        thead = self.head
        while thead:
            print(thead.element, end="==>")
            thead = thead.next
        print()

L = LinkedQueue()
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
