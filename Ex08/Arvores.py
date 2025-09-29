import random
import time
import bisect
import sys
sys.setrecursionlimit(200000)

# ----------------- Árvore Binária -----------------
class NodeBST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = NodeBST(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = NodeBST(key)
        else:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = NodeBST(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# ----------------- Árvore AVL -----------------
class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return NodeAVL(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# ----------------- Função de medição de tempo -----------------
def time_operation(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

# ----------------- Função para calcular altura -----------------
def calculate_height(node):
    if not node:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

# ----------------- Programa principal -----------------
N = 100_000
random.seed(42)
vector = random.sample(range(1, 1_000_000), N)  # vetor aleatório

search_keys = [50, 50_000]

# ----------------- 1) Vetor dados aleatórios -----------------
time_insert_vector = 0

times_search_vector = []
for key in search_keys:
    t, _ = time_operation(lambda k: k in vector, key)
    times_search_vector.append(t)

# ----------------- 2) Vetor ordenado + busca binária -----------------
start_sort = time.perf_counter()
vector_sorted = sorted(vector)
end_sort = time.perf_counter()
time_insert_sorted = end_sort - start_sort

times_search_sorted = []
for key in search_keys:
    t, _ = time_operation(lambda k: bisect.bisect_left(vector_sorted, k) < len(vector_sorted) and vector_sorted[bisect.bisect_left(vector_sorted, k)] == k, key)
    times_search_sorted.append(t)

# ----------------- 3) Árvore Binária -----------------
bst = BST()
start_bst = time.perf_counter()
for val in vector:
    bst.insert(val)
end_bst = time.perf_counter()
time_insert_bst = end_bst - start_bst

times_search_bst = []
for key in search_keys:
    t, _ = time_operation(bst.search, key)
    times_search_bst.append(t)

# Altura das subárvores BST
altura_esquerda_bst = calculate_height(bst.root.left)
altura_direita_bst = calculate_height(bst.root.right)

# ----------------- 4) Árvore AVL -----------------
avl = AVL()
start_avl = time.perf_counter()
for val in vector:
    avl.insert(val)
end_avl = time.perf_counter()
time_insert_avl = end_avl - start_avl

times_search_avl = []
for key in search_keys:
    t, _ = time_operation(avl.search, key)
    times_search_avl.append(t)

# Altura das subárvores AVL
altura_esquerda_avl = calculate_height(avl.root.left)
altura_direita_avl = calculate_height(avl.root.right)

# ----------------- Impressão dos resultados -----------------
print("\n--- Vetor dados aleatórios ---")
print(f"Tempo de inserção: {time_insert_vector:.6f} segundos")
print(f"Tempo de busca pelo elemento 50: {times_search_vector[0]:.6f} segundos")
print(f"Tempo de busca pelo elemento 50.000: {times_search_vector[1]:.6f} segundos")

print("\n--- Vetor ordenado + busca binária ---")
print(f"Tempo de inserção (ordenação): {time_insert_sorted:.6f} segundos")
print(f"Tempo de busca pelo elemento 50: {times_search_sorted[0]:.6f} segundos")
print(f"Tempo de busca pelo elemento 50.000: {times_search_sorted[1]:.6f} segundos")

print("\n--- Árvore Binária ---")
print(f"Tempo de inserção: {time_insert_bst:.6f} segundos")
print(f"Tempo de busca pelo elemento 50: {times_search_bst[0]:.6f} segundos")
print(f"Tempo de busca pelo elemento 50.000: {times_search_bst[1]:.6f} segundos")
print(f"Altura da subárvore esquerda: {altura_esquerda_bst}")
print(f"Altura da subárvore direita: {altura_direita_bst}")

print("\n--- Árvore AVL ---")
print(f"Tempo de inserção: {time_insert_avl:.6f} segundos")
print(f"Tempo de busca pelo elemento 50: {times_search_avl[0]:.6f} segundos")
print(f"Tempo de busca pelo elemento 50.000: {times_search_avl[1]:.6f} segundos")
print(f"Altura da subárvore esquerda: {altura_esquerda_avl}")
print(f"Altura da subárvore direita: {altura_direita_avl}")
