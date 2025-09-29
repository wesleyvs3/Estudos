import random
import time

vetor = [random.randint(0, 100000) for _ in range(100000)]

def primoFor(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primoRec(num, divisor=2):
    if num < 2:
        return False
    if divisor > int(num ** 0.5):
        return True
    if num % divisor == 0:
        return False
    return primoRec(num, divisor + 1)

def maiorPrimoFor(vetor):
    maior = -1
    for num in vetor:
        if primoFor(num) and num > maior:
            maior = num
    return maior

def maiorPrimoRec(vetor):
    maior = -1
    for num in vetor:
        if primoRec(num) and num > maior:
            maior = num
    return maior

tempoExecucao = time.time()
print(f"ITERATIVO -> Maior primo: {maiorPrimoFor(vetor)} | Tempo de execução: {time.time() - tempoExecucao} segundos")

tempoExecucao = time.time()
print(f"RECURSIVO -> Maior primo: {maiorPrimoRec(vetor)} | Tempo de execução: {time.time() - tempoExecucao} segundos")
