from queue_linkedlist import LinkedQueue
class BinaryTree:
    class Node:
        __slots__ = "element", "left", "right"
        
        def __init__(self, element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
        self.size = 0

    def make_tree(self, e, left, right):
        self.root = self.Node(e, left.root, right.root)
        left.root = None
        right.root = None

    def levelorder(self):
        Q = LinkedQueue()
        t = self.root
        print(t.element, end="==>")
        Q.enqueue(t)

        while not Q.is_Empty():
            t = Q.dequeue()
            if t.left:
                print(t.left.element, end="==>")
                Q.enqueue(t.left)
            if t.right:
                print(t.right.element, end="==>")
                Q.enqueue(t.right)

    def inorder(self, troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element, end="==>")
            self.inorder(troot.right)

    def preorder(self, troot):
        if troot:
            print(troot.element, end="==>")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element, end="==>")

a = BinaryTree()
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s= BinaryTree()
t = BinaryTree()

x.make_tree(40, a, a)
y.make_tree(60, a, a)
z.make_tree(20, x, a)
r.make_tree(50, a, y)
s.make_tree(30, r, a)
t.make_tree(10, z, s)

print("Levelorder")
t.levelorder()
print("\nPreorder")
t.preorder(t.root)
print("\nInorder")
t.inorder(t.root)
print("\nPostorder")
t.postorder(t.root)


