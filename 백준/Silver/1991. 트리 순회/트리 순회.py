import sys

def preorder(root):
    if root != ".":
        preorder_queue.append(root)
        preorder(edge[root][0])
        preorder(edge[root][1])

def inorder(root):
    if root != ".":
        inorder(edge[root][0])
        inorder_queue.append(root)
        inorder(edge[root][1])
        
def postorder(root):
    if root != ".":
        postorder(edge[root][0])
        postorder(edge[root][1])
        postorder_queue.append(root)
        
n = int(sys.stdin.readline())
tree = []
edge = dict()
for _ in range(n):
    node, left, right = sys.stdin.readline().split()
    edge[node] = [left, right]

preorder_queue = []
inorder_queue = []
postorder_queue = []
preorder("A")
inorder("A")
postorder("A")

for i in (preorder_queue, inorder_queue, postorder_queue):
    print("".join(i))