import random
import time

def gerarLista():
    lista = [random.randint(1, 100000) for _ in range(100000)]
    pos1, pos2 = random.sample(range(100000), 2)
    lista[pos1] = 9
    lista[pos2] = 99999
    return lista

def buscaSequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

vetor = gerarLista()

alvos = [9, 99999]

tempoExecucao = time.time()
for valor in alvos:
    posicao = buscaSequencial(vetor, valor)
    if posicao != -1:
        print(f"Valor {valor} encontrado na posição {posicao}")

print(f"Tempo de execução: {time.time() - tempoExecucao} segundos")
