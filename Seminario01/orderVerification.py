def verificar_ordenacao_parcial(nome_arquivo, linhas_verificacao=100):
    """Verifica se o arquivo está ordenado parcialmente (início, meio e fim)."""
    def esta_ordenado(lista):
        return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

    with open(nome_arquivo, 'r') as f:
        todas_linhas = f.readlines()
        total_linhas = len(todas_linhas)

        if total_linhas < linhas_verificacao * 3:
            print("Arquivo pequeno demais para verificação parcial confiável.")
            return False

        trecho_inicio = [int(l.strip()) for l in todas_linhas[:linhas_verificacao]]

        meio_inicio = total_linhas // 2 - linhas_verificacao // 2
        trecho_meio = [int(l.strip()) for l in todas_linhas[meio_inicio:meio_inicio + linhas_verificacao]]

        trecho_fim = [int(l.strip()) for l in todas_linhas[-linhas_verificacao:]]

        print("Verificando ordenação das 3 regiões do arquivo...")

        if not esta_ordenado(trecho_inicio):
            print("Início do arquivo não está ordenado.")
            return False
        if not esta_ordenado(trecho_meio):
            print("Meio do arquivo não está ordenado.")
            return False
        if not esta_ordenado(trecho_fim):
            print("Fim do arquivo não está ordenado.")
            return False

        print("As 3 regiões verificadas estão ordenadas.")
        return True

if __name__ == "__main__":
    verificar_ordenacao_parcial("disordered_data.txt")
