import random

# Configurando a semente para resultados reproduzíveis (opcional)
random.seed(10)

# Criando a matriz 12x12 com números aleatórios de 0 a 10
M = [[random.randint(0, 10) for _ in range(12)] for _ in range(12)]

# Lendo o caractere de operação
operacao = input("Digite 'S' para soma ou 'M' para média: ").upper()

# Inicializando variáveis para soma e contagem
soma = 0
contagem = 0

# Calculando soma ou média dos elementos acima da diagonal secundária
for i in range(12):
    for j in range(12):
        if j < 11 - i:  # Acima da diagonal secundária
            soma += M[i][j]
            contagem += 1

# Exibindo a matriz
print("Matriz criada:")
for linha in M:
    for num in linha:
        print("%3d" % num, end=' ')
    print()  # Nova linha após cada linha da matriz

# Calculando o resultado baseado na operação escolhida
if operacao == 'S':
    resultado = soma
elif operacao == 'M':
    resultado = soma // contagem if contagem > 0 else 0

# Exibindo o resultado da operação
print(f"Resultado da conta: {resultado}")
