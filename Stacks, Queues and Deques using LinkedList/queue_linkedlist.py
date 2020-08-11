from exceptions import Empty

class LinkedQueue:
    class Node:
        __slots__ = "element", "next"

        def __init__(self, element, next):
            self.element = element
            self.next = next
    
    def __init__(self):
        self.head  = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_Empty(self):
        return self.size == 0

    def enqueue(self, e):
        n1 = self.Node(e, None)
        if self.is_Empty():
            self.head = n1
        else:
            self.tail.next = n1
        self.tail = n1
        self.size += 1

    def dequeue(self):
        if self.is_Empty():
            raise Empty("queue is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -= 1 
        if self.is_Empty():
            self.tail = None
        return value

    def first(self):
        if self.is_Empty():
            raise Empty ("queue is empty")
        return self.head.element
    
    def display(self):
        thead = self.head
        while thead:
            print(thead.element, end="==>")
            thead = thead.next
        print()

q = LinkedQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
print("Length: ", len(q))
print("Dequeue: ", q.dequeue())
q.display()
q.enqueue(50)
q.enqueue(60)
q.display()
print("1st element: ", q.first())
q.display()
print("Dequeue: ", q.dequeue())
q.display()