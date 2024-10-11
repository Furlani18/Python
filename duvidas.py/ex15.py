# Função para solicitar ao usuário os elementos da matriz 3x3
def receber_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

# Função para calcular a soma dos elementos da diagonal principal
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][i]
    return soma

# Função para imprimir a matriz
def imprimir_matriz(matriz):
    print("Matriz 3x3:")
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4}", end=" ")
        print()

# Programa principal
matriz = receber_matriz()
imprimir_matriz(matriz)
soma = soma_diagonal_principal(matriz)
print(f"Soma dos elementos da diagonal principal: {soma}")
