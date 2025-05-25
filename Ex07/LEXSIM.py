import sys

precedencia = {'^': 6, '*': 5, '/': 5, '+': 4, '-': 4, '>': 3, '<': 3, '=': 3, '#': 3, '.': 2, '|': 1}

def eh_operador(c):
    return c in precedencia

def eh_operando(c):
    return c.isalpha() or c.isdigit()

def analise_lexica(expr):
    for c in expr:
        if not (eh_operador(c) or eh_operando(c) or c in '()'):
            return False
    return True

def analise_sintatica(expr):
    par = 0
    prev = ''
    for i, c in enumerate(expr):
        if c == '(':
            par += 1
        elif c == ')':
            par -= 1
            if par < 0:
                return False
        elif eh_operador(c):
            if i == 0 or i == len(expr) -1:
                return False
            if prev and eh_operador(prev):
                return False
        elif eh_operando(c):
            if prev and eh_operando(prev):
                return False
        prev = c
    if par != 0:
        return False
    return True

def infixa_para_posfixa(expr):
    saida = []
    pilha = []
    
    for c in expr:
        if eh_operando(c):
            saida.append(c)
        elif c == '(':
            pilha.append(c)
        elif c == ')':
            while pilha and pilha[-1] != '(':
                saida.append(pilha.pop())
            pilha.pop()
        elif eh_operador(c):
            while (pilha and pilha[-1] != '(' and
                   precedencia.get(c, 0) <= precedencia.get(pilha[-1], 0)):
                saida.append(pilha.pop())
            pilha.append(c)
    
    while pilha:
        saida.append(pilha.pop())
    
    return ''.join(saida)

for linha in sys.stdin:
    expr = linha.strip().replace(' ', '')
    if not expr:
        continue
    if not analise_lexica(expr):
        print("Lexical Error!")
    elif not analise_sintatica(expr):
        print("Syntax Error!")
    else:
        posfixa = infixa_para_posfixa(expr)
        print(posfixa)
