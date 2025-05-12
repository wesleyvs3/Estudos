import random
import time
from collections import namedtuple

# Estrutura de dados para armazenar as datas
Data = namedtuple("Data", ["dia", "mes", "ano"])

# Gerar vetor de 1000 datas aleatórias
def gerar_datas(qtd=1000):
    return [Data(random.randint(1, 31), random.randint(1, 12), random.randint(2000, 2024)) for _ in range(qtd)]

# Função de Counting Sort (Estável)
def counting_sort(arr, key, max_val):
    count = [0] * (max_val + 1)
    output = [None] * len(arr)

    for data in arr:
        count[getattr(data, key)] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for data in reversed(arr):
        output[count[getattr(data, key)] - 1] = data
        count[getattr(data, key)] -= 1

    return output

# Função de Merge Sort (Estável)
def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Função de QuickSort (Não Estável)
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = getattr(arr[len(arr) // 2], key)
    left = [x for x in arr if getattr(x, key) < pivot]
    middle = [x for x in arr if getattr(x, key) == pivot]
    right = [x for x in arr if getattr(x, key) > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# Radix Sort com Counting Sort (Estável)
def radix_sort_contagem(arr):
    arr = counting_sort(arr, "dia", 31)
    arr = counting_sort(arr, "mes", 12)
    arr = counting_sort(arr, "ano", 2024)
    return arr

# Radix Sort com Merge Sort (Estável)
def radix_sort_merge(arr):
    arr = counting_sort(arr, "dia", 31)
    arr = merge_sort(arr, "mes")
    arr = merge_sort(arr, "ano")
    return arr

# Radix Sort com QuickSort (Não Estável)
def radix_sort_quick(arr):
    arr = counting_sort(arr, "dia", 31)
    arr = quick_sort(arr, "mes")
    arr = quick_sort(arr, "ano")
    return arr

# Gerando 1000 datas aleatórias
dados = gerar_datas()

# Medindo tempos de execução
start = time.time()
ordenado_contagem = radix_sort_contagem(dados)
tempo_contagem = time.time() - start

start = time.time()
ordenado_merge = radix_sort_merge(dados)
tempo_merge = time.time() - start

start = time.time()
ordenado_quick = radix_sort_quick(dados)
tempo_quick = time.time() - start

# Comparação dos tempos
print(f"Tempo Radix com Counting Sort (estável): {tempo_contagem:.6f} segundos")
print(f"Tempo Radix com Merge Sort (estável): {tempo_merge:.6f} segundos")
print(f"Tempo Radix com QuickSort (instável): {tempo_quick:.6f} segundos")

# Comentário sobre falha na ordenação
print("\nExplicação: QuickSort é um algoritmo não estável, então ele pode desorganizar elementos já parcialmente ordenados. Isso pode fazer com que dias e meses sejam reordenados de maneira errada.")
