class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if node is None or node.data == key:
            return node

        if node.data < key:
            return self.search(node.right, key)

        return self.search(node.left, key)

    def insert(self, node, key):
        if node is None:
            return Node(key)

        if node.data < key:
            node.right = self.insert(node.right, key)
        else:
            node.left = self.insert(node.left, key)

        return node

    def minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def maximum(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)

        current = self.root
        successor = None

        while current is not None:
            if node.data < current.data:
                successor = current
                current = current.left
            elif node.data > current.data:
                current = current.right
            else:
                break

        return successor

    def delete(self, node, key):
        if node is None:
            return node

        if key < node.data:
            node.left = self.delete(node.left, key)
        elif key > node.data:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.minimum(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)

        return node

# Create an empty BST
bst = BinarySearchTree()

# Insert nodes into the BST
bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 20)
bst.root = bst.insert(bst.root, 40)
bst.root = bst.insert(bst.root, 70)
bst.root = bst.insert(bst.root, 60)
bst.root = bst.insert(bst.root, 80)

# Search for a node in the BST
search_node = bst.search(bst.root, 60)

# Get the maximum element in the BST
max_node = bst.maximum(bst.root)

# Get the minimum element in the BST
min_node = bst.minimum(bst.root)

# Get the successor of a node in the BST
successor_node = bst.successor(search_node)

# Delete a node from the BST
bst.root = bst.delete(bst.root, 40)
