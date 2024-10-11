numeros = []

def adicionar_numero():
    while True:
        numero = input("Digite um número (ou 'air' para parar de adicionar números): ")
        if numero.lower() == 'air':
            break
        try:
            numeros.append(float(numero))
        except ValueError:
            print("Erro: você deve digitar um número válido")

def calcular_media():
    if len(numeros) < 2:
        print("Você precisa adicionar pelo menos 2 números à lista")
        return
    media = sum(numeros) / len(numeros)
    print("A média é:", media)

def calcular_mediana():
    if len(numeros) < 2:
        print("Você precisa adicionar pelo menos 2 números à lista")
        return
    numeros.sort()
    tamanho_lista = len(numeros)
    if tamanho_lista % 2!= 0:
        mediana = numeros[tamanho_lista // 2]
    else:
        mediana = (numeros[tamanho_lista // 2 - 1] + numeros[tamanho_lista // 2]) / 2
    print("A mediana é:", mediana)

def calcular_moda():
    if len(numeros) < 2:
        print("Você precisa adicionar pelo menos 2 números à lista")
        return
    moda = max(set(numeros), key=numeros.count)
    print("A moda é:", moda)

def mostrar_lista():
    print("Lista de números:", numeros)

# Exemplo de uso
print("Digite os números que você deseja adicionar à lista (digite 'air' para parar de adicionar números):")
adicionar_numero()
mostrar_lista()
calcular_media()
calcular_mediana()
calcular_moda()