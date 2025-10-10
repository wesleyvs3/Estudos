from PIL import Image
import numpy as np
import os

def aumentar_contraste(imagem_array, fator=1.2):
    altura, largura = imagem_array.shape
    soma = 0

    for i in range(altura):
        for j in range(largura):
            soma += int(imagem_array[i][j])

    media = soma // (altura * largura)

    imagem_contrastada = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            valor = int(imagem_array[i][j])
            novo_valor = (valor - media) * fator + media
            novo_valor = max(0, min(255, int(novo_valor)))
            imagem_contrastada[i][j] = novo_valor

    return imagem_contrastada

def calcular_limiar_mediana(imagem_array):
    altura, largura = imagem_array.shape
    tons = []

    for i in range(altura):
        for j in range(largura):
            tons.append(int(imagem_array[i][j]))

    tons.sort()
    meio = len(tons) // 2
    return tons[meio]

def aplicar_limiarizacao(imagem_array, limiar):
    altura, largura = imagem_array.shape
    imagem_segmentada = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            if imagem_array[i][j] > limiar:
                imagem_segmentada[i][j] = 255
            else:
                imagem_segmentada[i][j] = 0

    return imagem_segmentada

pasta_imagens = "./Shenzhen/img"
os.makedirs("segmentadas_pulmao", exist_ok=True)

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith((".jpg", ".png")):
        caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
        imagem = Image.open(caminho_imagem).convert("L")
        imagem_array = np.array(imagem)

        imagem_contrastada = aumentar_contraste(imagem_array, fator=1.6)

        limiar = calcular_limiar_mediana(imagem_contrastada)

        imagem_segmentada = aplicar_limiarizacao(imagem_contrastada, limiar)

        Image.fromarray(imagem_segmentada).save(f"segmentadas_pulmao/{nome_arquivo}")

print("Segmentação com contraste concluída com sucesso!")
