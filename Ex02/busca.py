import random
import time

def gerarLista():
    lista = [random.randint(1, 100000) for _ in range(100000)]
    pos1, pos2 = random.sample(range(100000), 2)
    lista[pos1] = 9
    lista[pos2] = 99999
    return lista

#quicksort:
def ordenarLista(lista):
    if len(lista) <= 1:
        return lista
    menores = [x for x in lista[1:] if x <= lista[0]]
    maiores = [x for x in lista[1:] if x > lista[0]]
    return ordenarLista(menores) + [lista[0]] + ordenarLista(maiores)

def buscaBinaria(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] > alvo:
        return buscaBinaria(lista, alvo, inicio, meio - 1)
    else:
        return buscaBinaria(lista, alvo, meio + 1, fim)

def buscaSequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# Geração da lista original
vetorOriginal = gerarLista()
alvos = [9, 99999]

# Busca Sequencial
print("Busca Sequencial:")
tempoInicioSeq = time.time()
for valor in alvos:
    posicao = buscaSequencial(vetorOriginal, valor)
    if posicao != -1:
        print(f"Valor {valor} encontrado na posição {posicao}")
    else:
        print(f"Valor {valor} não encontrado")
tempoTotalSeq = time.time() - tempoInicioSeq
print(f"Tempo de execução (sequencial): {tempoTotalSeq} segundos\n")

# Busca Binária
print("Busca Binária:")
tempoInicioBin = time.time()
vetorOrdenado = ordenarLista(vetorOriginal)
for valor in alvos:
    posicao = buscaBinaria(vetorOrdenado, valor, 0, len(vetorOrdenado) - 1)
    if posicao != -1:
        print(f"Valor {valor} encontrado na posição {posicao}")
    else:
        print(f"Valor {valor} não encontrado")
tempoTotalBin = time.time() - tempoInicioBin
print(f"Tempo de execução (binária + ordenação): {tempoTotalBin} segundos")
