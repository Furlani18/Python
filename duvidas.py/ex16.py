import random

# Função para criar uma matriz 10x5 com números inteiros aleatórios
def criar_matriz():
    matriz = []
    for i in range(10):
        linha = [random.randint(1, 100) for _ in range(5)]
        matriz.append(linha)
    return matriz

# Função para calcular a matriz transposta
def transpor_matriz(matriz):
    matriz_transposta = []
    for j in range(len(matriz[0])):
        linha_transposta = [matriz[i][j] for i in range(len(matriz))]
        matriz_transposta.append(linha_transposta)
    return matriz_transposta

# Função para imprimir uma matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4}", end=" ")
        print()

# Programa principal
matriz = criar_matriz()
print("Matriz original (10x5):")
imprimir_matriz(matriz)

matriz_transposta = transpor_matriz(matriz)
print("\nMatriz transposta (5x10):")
imprimir_matriz(matriz_transposta)
