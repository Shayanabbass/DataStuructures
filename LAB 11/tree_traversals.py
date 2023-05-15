class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_recursive(root):
    if root:
        print(root.data, end='')
        preorder_recursive(root.left)
        preorder_recursive(root.right)

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.data, end='')
        inorder_recursive(root.right)

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.data, end='')

def preorder_nonrecursive(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        print(node.data, end='')
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def inorder_nonrecursive(root):
    if root is None:
        return
    stack = []
    node = root
    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        elif len(stack) != 0:
            node = stack.pop()
            print(node.data, end='')
            node = node.right
        else:
            break

def postorder_nonrecursive(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) != 0:
        node = stack1.pop()
        stack2.append(node)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
    while len(stack2) != 0:
        node = stack2.pop()
        print(node.data, end='')

# create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# traverse the binary tree recursively
print("Recursive Pre-order Traversal:")
preorder_recursive(root)
print("\nRecursive In-order Traversal:")
inorder_recursive(root)
print("\nRecursive Post-order Traversal:")
postorder_recursive(root)

# traverse the binary tree non-recursively
print("\nNon-recursive Pre-order Traversal:")
preorder_nonrecursive(root)
print("\nNon-recursive In-order Traversal:")
inorder_nonrecursive(root)
print("\nNon-recursive Post-order Traversal:")
postorder_nonrecursive(root)
