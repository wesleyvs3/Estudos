import os
import random
import time

TAM_BLOCO = 1_000_000
nome_arquivo = "disordered_data.txt"

def escolher_pivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()
        return int(random.choice(linhas).strip())

def particionar_arquivo(nome_arquivo, pivo, arq_menor, arq_maior, arq_iguais):
    with open(nome_arquivo, 'r') as entrada, \
         open(arq_menor, 'w') as fmenor, \
         open(arq_maior, 'w') as fmaior, \
         open(arq_iguais, 'w') as figual:
        
        for linha in entrada:
            num = int(linha.strip())
            if num < pivo:
                fmenor.write(f"{num}\n")
            elif num > pivo:
                fmaior.write(f"{num}\n")
            else:
                figual.write(f"{num}\n")

def ordenar_arquivo_em_memoria(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        dados = [int(l.strip()) for l in f]
    dados.sort()
    with open(nome_arquivo, 'w') as f:
        for num in dados:
            f.write(f"{num}\n")

def tamanho_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return sum(1 for _ in f)

def quicksort_externo(nome_arquivo, limite_ram=TAM_BLOCO):
    if tamanho_arquivo(nome_arquivo) <= limite_ram:
        ordenar_arquivo_em_memoria(nome_arquivo)
        return

    pivo = escolher_pivo(nome_arquivo)

    menor = nome_arquivo + "_menor"
    maior = nome_arquivo + "_maior"
    iguais = nome_arquivo + "_iguais"

    particionar_arquivo(nome_arquivo, pivo, menor, maior, iguais)

    quicksort_externo(menor, limite_ram)
    quicksort_externo(maior, limite_ram)

    with open(nome_arquivo, 'w') as saida:
        for nome_parte in [menor, iguais, maior]:
            with open(nome_parte, 'r') as parte:
                for linha in parte:
                    saida.write(linha)

    os.remove(menor)
    os.remove(maior)
    os.remove(iguais)

if __name__ == "__main__":
    inicio = time.time()
    quicksort_externo(nome_arquivo, limite_ram=TAM_BLOCO)
    fim = time.time()
    duracao = fim - inicio
    print(f"Ordenação concluída em {duracao:.2f} segundos.")
