from exceptions import Empty

class LinkedStack:
    class Node :
        __slots__ = "element", "next"
        
        def __init__(self, element, next):
            self.element = element
            self.next = next
   
    def __init__(self):
        self.size = 0
        self.head = None
    
    def __len__(self):
        return self.size

    def is_Empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1

    def pop(self):
        if self.is_Empty():
            raise Empty("Stack is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        return value

    def top(self):
        if self.is_Empty():
            raise Empty("Stack is empty")
        return self.head.element

    def display(self):
        thead = self.head
        while thead:
            print(thead.element, end= "==>")
            thead = thead.next
        print()

ls = LinkedStack()
ls.push(10)
ls.push(20)
ls.push(30)
ls.push(40)
ls.display()
print("Popped: ", ls.pop())
ls.display()
ls.push(70)
ls.display()
print("Top element: ", ls.top())
ls.display()
print("Popped: ", ls.pop())
ls.display()
