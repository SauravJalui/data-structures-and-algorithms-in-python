from exceptions import Empty

class DoublyLinkedList:
    class Node:
        __slots__ = "element", "prev", "next"
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
            
    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add_first(self, e):
        n1 = self.Node(e, None, None)
        if self.isEmpty():
            self.head = n1
            self.tail = n1
        else:
            n1.next = self.head
            self.head.prev = n1
        self.head = n1
        self.size += 1

    def add_last(self, e):
        n1 = self.Node(e, None, None)
        if self.isEmpty():
            self.head = n1
            self.tail = n1 
        else:
            self.tail.next = n1
            n1.prev = self.tail
        self.tail = n1
        self.size += 1

    def add_any(self, e, pos):
        n1 = self.Node(e, None, None)
        thead = self.head
        i = 1
        while i < pos - 1:
            thead = thead.next
            i += 1
        n1.next = thead.next
        thead.next = n1
        thead.next.prev = n1
        n1.prev = thead
        self.size += 1
    
    def remove_first(self):
        if self.isEmpty():
            raise Empty("List is empty")
        value = self.head.element
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        if self.isEmpty():
            self.tail = None
        return value

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
        value = thead.element
        self.tail.next = None
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
        thead.next.next.prev = thead
        self.size -= 1
        return value

    def display(self):
        thead = self.head
        while thead:
            print(thead.element, end = "==>")
            thead = thead.next
        print()

DL = DoublyLinkedList()
DL.add_last(10)
DL.add_last(20)
DL.add_last(30)
DL.add_last(40)
DL.display()
print("Deleted : ", DL.remove_first())
DL.display()
DL.add_first(70)
DL.display()
print("Deleted : ", DL.remove_last())
DL.display()
DL.add_any( 100, 2)
DL.display()
print("Deleted:" ,DL.remove_any(2))
DL.display()






        



