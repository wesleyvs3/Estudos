import sys

ligacao = {'B': 'S', 'S': 'B', 'C': 'F', 'F': 'C'}

for linha in sys.stdin:
    fita = linha.strip()
    pilha = []
    ligacoes = 0

    for base in fita:
        if pilha and ligacao[base] == pilha[-1]:
            pilha.pop()
            ligacoes += 1
        else:
            pilha.append(base)

    print(ligacoes)