import random
import time

class Node:
    def __init__(self, key, color, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color='black')
        self.root = self.NIL

    def insert(self, key):
        node = Node(key, 'red', left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def search(self, key):
        current = self.root
        while current != self.NIL and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current != self.NIL

tree = RedBlackTree()

elements = random.sample(range(1, 200000), 100000)

start_insert = time.perf_counter()
for number in elements:
    tree.insert(number)
end_insert = time.perf_counter()
insert_time = end_insert - start_insert

start_search_50 = time.perf_counter()
tree.search(50)
end_search_50 = time.perf_counter()
search_50_time = end_search_50 - start_search_50

start_search_50000 = time.perf_counter()
tree.search(50000)
end_search_50000 = time.perf_counter()
search_50000_time = end_search_50000 - start_search_50000

def height(node):
    if node is None or node.key is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

left_subtree_height = height(tree.root.left)
right_subtree_height = height(tree.root.right)

# Resultados
print(f"Tempo de inserção de 100.000 elementos: {insert_time:.6f} segundos")
print(f"Tempo de busca pelo valor 50: {search_50_time:.6f} segundos")
print(f"Tempo de busca pelo valor 50.000: {search_50000_time:.6f} segundos")
print(f"Altura da subárvore esquerda: {left_subtree_height}")
print(f"Altura da subárvore direita: {right_subtree_height}")