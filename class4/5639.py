import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)

    def insert_recursive(self, root, data):
        if data > root.data:
            if root.right == None:
                root.right = Node(data)
            else:
                self.insert_recursive(root.right, data)
        else:
            if root.left == None:
                root.left = Node(data)
            else:
                self.insert_recursive(root.left, data)

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.data)

tree = BinarySearchTree()

while(True):
    try:
        num = int(input())
        tree.insert(num)
    except:
        break

post_order(tree.root)