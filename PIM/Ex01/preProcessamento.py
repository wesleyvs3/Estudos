import kagglehub
from PIL import Image
import numpy as np
import os
import random

def adicionar_ruido_sal_pimenta(imagem_array, proporcao_sal=0.01, proporcao_pimenta=0.01):
    imagem_ruidosa = imagem_array.copy()
    linhas, colunas = imagem_ruidosa.shape

    quantidade_sal = int(proporcao_sal * linhas * colunas)
    quantidade_pimenta = int(proporcao_pimenta * linhas * colunas)

    for _ in range(quantidade_sal):
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        imagem_ruidosa[i, j] = 255

    for _ in range(quantidade_pimenta):
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        imagem_ruidosa[i, j] = 0

    return imagem_ruidosa

def aplicar_filtro_media(imagem_array, tamanho_kernel=3):
    borda = tamanho_kernel // 2
    altura, largura = imagem_array.shape
    imagem_suavizada = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            soma = 0
            contador = 0
            for ki in range(-borda, borda + 1):
                for kj in range(-borda, borda + 1):
                    ni = min(max(i + ki, 0), altura - 1)
                    nj = min(max(j + kj, 0), largura - 1)
                    soma += imagem_array[ni][nj]
                    contador += 1
            media = round(soma / contador)
            imagem_suavizada[i][j] = media

    return imagem_suavizada

def aplicar_filtro_mediana(imagem_array, tamanho_kernel=3):
    borda = tamanho_kernel // 2
    altura, largura = imagem_array.shape
    imagem_suavizada = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            vizinhos = []
            for ki in range(-borda, borda + 1):
                for kj in range(-borda, borda + 1):
                    ni = min(max(i + ki, 0), altura - 1)
                    nj = min(max(j + kj, 0), largura - 1)
                    vizinhos.append(imagem_array[ni][nj])
            vizinhos.sort()
            mediana = vizinhos[len(vizinhos) // 2]
            imagem_suavizada[i][j] = mediana

    return imagem_suavizada

def aplicar_filtro_minimo(imagem_array, tamanho_kernel=3):
    borda = tamanho_kernel // 2
    altura, largura = imagem_array.shape
    imagem_suavizada = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            minimo = 255
            for ki in range(-borda, borda + 1):
                for kj in range(-borda, borda + 1):
                    ni = min(max(i + ki, 0), altura - 1)
                    nj = min(max(j + kj, 0), largura - 1)
                    valor = imagem_array[ni][nj]
                    if valor < minimo:
                        minimo = valor
            imagem_suavizada[i][j] = minimo

    return imagem_suavizada

caminho_dataset = kagglehub.dataset_download("masoudnickparvar/brain-tumor-mri-dataset")
print("Caminho para os arquivos do dataset:", caminho_dataset)

pasta_imagens = os.path.join(caminho_dataset, "Testing", "glioma")

os.makedirs("imagens_com_ruido", exist_ok=True)
os.makedirs("imagens_suavizadas_media", exist_ok=True)
os.makedirs("imagens_suavizadas_mediana", exist_ok=True)
os.makedirs("imagens_suavizadas_minimo", exist_ok=True)

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith((".jpg", ".png")):
        caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
        imagem = Image.open(caminho_imagem).convert("L")
        imagem_array = np.array(imagem)

        imagem_ruidosa = adicionar_ruido_sal_pimenta(imagem_array)
        Image.fromarray(imagem_ruidosa).save(f"imagens_com_ruido/{nome_arquivo}")

        suavizada_media = aplicar_filtro_media(imagem_ruidosa)
        suavizada_mediana = aplicar_filtro_mediana(imagem_ruidosa)
        suavizada_minimo = aplicar_filtro_minimo(imagem_ruidosa)

        Image.fromarray(suavizada_media).save(f"imagens_suavizadas_media/{nome_arquivo}")
        Image.fromarray(suavizada_mediana).save(f"imagens_suavizadas_mediana/{nome_arquivo}")
        Image.fromarray(suavizada_minimo).save(f"imagens_suavizadas_minimo/{nome_arquivo}")

print("Processamento concluído com todos os filtros!")
