from queue_linkedlist import LinkedQueue

class BinarySearchTree:
    class Node:
        __slots__ = "element",  "left", "right"

        def __init__(self, element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, e):
        troot = self.root
        ttroot = None
        while troot:
            ttroot = troot
            if e < troot.element:
                troot = troot.left
            elif e > troot.element:
                troot = troot.right
        node = self.Node(e)
        if self.root:
            if e < ttroot.element:
                ttroot.left = node
            else:
                ttroot.right = node
        else:
            self.root = node

    def recurinsert(self, troot, e):
        if troot == None:
            node = self.Node(e)
            return node

        if e < troot.element:
            troot.left = self.recurinsert(troot.left, e)
        elif e > troot.element:
            troot.right = self.recurinsert(troot.right, e)

        return troot



    def search(self, k):
        troot = self.root
        while troot:
            if k < troot.element:
                troot = troot.left
            elif k > troot.element:
                troot = troot.right
            else:
                return True
        return False

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

B = BinarySearchTree()
B.root = B.recurinsert(None, 70)
B.recurinsert(B.root, 70)
B.recurinsert(B.root,30)
B.recurinsert(B.root,90)
B.recurinsert(B.root,40)
B.recurinsert(B.root,50)
B.recurinsert(B.root,110)
B.inorder(B.root)
print(B.search(45))