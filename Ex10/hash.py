import time
import random

def hash_divisao(key, m):
    return key % m

class HashEncadeamento:
    def __init__(self, m):
        self.m = m
        self.tabela = [[] for _ in range(m)]

    def inserir(self, key):
        h = hash_divisao(key, self.m)
        if key not in self.tabela[h]:
            self.tabela[h].append(key)

    def buscar(self, key):
        h = hash_divisao(key, self.m)
        return key in self.tabela[h]

class HashSondagemLinear:
    def __init__(self, m):
        self.m = m
        self.tabela = [None] * m

    def inserir(self, key):
        h = hash_divisao(key, self.m)
        inicial = h
        while self.tabela[h] is not None:
            if self.tabela[h] == key:
                return
            h = (h + 1) % self.m
            if h == inicial:
                raise Exception("Tabela cheia")
        self.tabela[h] = key

    def buscar(self, key):
        h = hash_divisao(key, self.m)
        inicial = h
        while self.tabela[h] is not None:
            if self.tabela[h] == key:
                return True
            h = (h + 1) % self.m
            if h == inicial:
                break
        return False

# Geração dos dados
random.seed(42)
elementos = random.sample(range(100_001), 100_000)

# Encadeamento
hash_enc = HashEncadeamento(50_000)
t0 = time.perf_counter()
for x in elementos:
    hash_enc.inserir(x)
t1 = time.perf_counter()
t2 = time.perf_counter()
busca_enc = hash_enc.buscar(10_000)
t3 = time.perf_counter()

# Endereçamento aberto
hash_aberto = HashSondagemLinear(100_000)
t4 = time.perf_counter()
for x in elementos:
    hash_aberto.inserir(x)
t5 = time.perf_counter()
t6 = time.perf_counter()
busca_aberto = hash_aberto.buscar(10_000)
t7 = time.perf_counter()

# Resultados
print(f"Encadeamento:")
print(f"  Tempo de inserção: {(t1 - t0):.6f} segundos")
print(f"  Tempo de busca:    {(t3 - t2):.10f} segundos")
print(f"  Elemento 10.000 encontrado? {busca_enc}")

print(f"\nEndereçamento Aberto:")
print(f"  Tempo de inserção: {(t5 - t4):.6f} segundos")
print(f"  Tempo de busca:    {(t7 - t6):.10f} segundos")
print(f"  Elemento 10.000 encontrado? {busca_aberto}")
