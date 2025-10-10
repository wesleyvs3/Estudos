from PIL import Image
import numpy as np
import os

def filtro_mediana_manual(imagem_array, tamanho_kernel=3):
    borda = tamanho_kernel // 2
    altura, largura = imagem_array.shape
    resultado = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            vizinhos = []
            for ki in range(-borda, borda + 1):
                for kj in range(-borda, borda + 1):
                    ni = min(max(i + ki, 0), altura - 1)
                    nj = min(max(j + kj, 0), largura - 1)
                    vizinhos.append(imagem_array[ni][nj])
            vizinhos.sort()
            resultado[i][j] = vizinhos[len(vizinhos) // 2]

    return resultado

def aumentar_contraste(imagem_array, fator=1.5):
    altura, largura = imagem_array.shape
    soma = 0
    for i in range(altura):
        for j in range(largura):
            soma += int(imagem_array[i][j])
    media = soma // (altura * largura)

    resultado = np.zeros((altura, largura), dtype=np.uint8)
    for i in range(altura):
        for j in range(largura):
            valor = int(imagem_array[i][j])
            novo_valor = (valor - media) * fator + media
            resultado[i][j] = max(0, min(255, int(novo_valor)))
    return resultado

def gradiente_local(imagem_array):
    altura, largura = imagem_array.shape
    resultado = np.zeros((altura, largura), dtype=np.uint8)
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            centro = int(imagem_array[i][j])
            vizinhos = [
                int(imagem_array[i-1][j]), int(imagem_array[i+1][j]),
                int(imagem_array[i][j-1]), int(imagem_array[i][j+1])
            ]
            variacao = sum(abs(centro - v) for v in vizinhos) // len(vizinhos)
            resultado[i][j] = variacao
    return resultado

def criar_marcadores(imagem_array, limiar_vale=80, limiar_montanha=180):
    altura, largura = imagem_array.shape
    marcadores = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            valor = imagem_array[i][j]
            if valor < limiar_vale:
                marcadores[i][j] = 1
            elif valor > limiar_montanha:
                marcadores[i][j] = 2

    return marcadores

def watershed_manual(marcadores, gradiente, iteracoes=5):
    altura, largura = marcadores.shape
    resultado = marcadores.copy()

    for _ in range(iteracoes):
        novo = resultado.copy()
        for i in range(1, altura - 1):
            for j in range(1, largura - 1):
                if resultado[i][j] == 0:
                    vizinhos = [
                        resultado[i-1][j], resultado[i+1][j],
                        resultado[i][j-1], resultado[i][j+1]
                    ]
                    vizinhos_validos = [v for v in vizinhos if v in [1, 2]]
                    if len(set(vizinhos_validos)) == 1:
                        novo[i][j] = vizinhos_validos[0]
                    elif len(set(vizinhos_validos)) > 1:
                        novo[i][j] = 3
        resultado = novo

    imagem_segmentada = np.zeros((altura, largura), dtype=np.uint8)
    for i in range(altura):
        for j in range(largura):
            if resultado[i][j] == 1:
                imagem_segmentada[i][j] = 255
            elif resultado[i][j] == 3:
                imagem_segmentada[i][j] = 128

    return imagem_segmentada

pasta_imagens = "./Shenzhen/img"
os.makedirs("segmentadas_pulmao_watershed", exist_ok=True)

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith((".jpg", ".png")):
        caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
        imagem = Image.open(caminho_imagem).convert("L")
        imagem_array = np.array(imagem)

        suavizada = filtro_mediana_manual(imagem_array)
        contrastada = aumentar_contraste(suavizada, fator=3)
        gradiente = gradiente_local(contrastada)
        marcadores = criar_marcadores(contrastada, limiar_vale=200, limiar_montanha=150)
        segmentada = watershed_manual(marcadores, gradiente, iteracoes=1)

        Image.fromarray(segmentada).save(f"segmentadas_pulmao_watershed/{nome_arquivo}")

print("Segmentação Watershed manual concluída com sucesso!")
