class Node:
    def __init__(self, root, left, right):
        self.left = left
        self.root = root
        self.right = right

def pre_order(node):
    print(node.root, end='')
    if node.left:
        pre_order(arr[node.left])
    if node.right:
        pre_order(arr[node.right])

def in_order(node):
    if node.left:
        in_order(arr[node.left])
    print(node.root, end='')
    if node.right:
        in_order(arr[node.right])

def post_order(node):
    if node.left:
        post_order(arr[node.left])
    if node.right:
        post_order(arr[node.right])
    print(node.root, end='')

N = int(input())
arr = {}

for _ in range(N):
    a, b, c = map(str, input().split())
    left, right = b, c
    if b == '.':
        left = None
    if c == '.':
        right = None
    arr[a] = Node(a, left, right)

pre_order(arr['A'])
print()
in_order(arr['A'])
print()
post_order(arr['A'])