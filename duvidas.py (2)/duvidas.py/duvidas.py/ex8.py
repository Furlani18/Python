import time

# Dicionário para armazenar informações sobre os carros
estoque_carros = {}

# Funções para gerenciar o estoque de carros
def adicionar_carro():
    modelo = input("Digite o modelo do carro: ")
    preco = float(input("Digite o preço do carro: "))
    quantidade = int(input("Digite a quantidade de carros: "))
    estoque_carros[modelo] = {'preço': preco, 'quantidade': quantidade}
    print(f"Carro {modelo} adicionado com sucesso.")

def excluir_carro():
    modelo = input("Digite o modelo do carro que deseja excluir: ")
    if modelo in estoque_carros:
        del estoque_carros[modelo]
        print(f"Carro {modelo} excluído com sucesso.")
    else:
        print(f"Carro {modelo} não encontrado no estoque.")

def alterar_preco():
    modelo = input("Digite o modelo do carro que deseja alterar o preço: ")
    if modelo in estoque_carros:
        novo_preco = float(input("Digite o novo preço: "))
        estoque_carros[modelo]['preço'] = novo_preco
        print(f"Preço do carro {modelo} alterado com sucesso.")
    else:
        print(f"Carro {modelo} não encontrado no estoque.")

def modificar_quantidade():
    modelo = input("Digite o modelo do carro que deseja alterar a quantidade: ")
    if modelo in estoque_carros:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        estoque_carros[modelo]['quantidade'] = nova_quantidade
        print(f"Quantidade do carro {modelo} alterada com sucesso.")
    else:
        print(f"Carro {modelo} não encontrado no estoque.")

def imprimir_estoque():
    if not estoque_carros:
        print("O estoque está vazio.")
    else:
        for modelo, detalhes in estoque_carros.items():
            print(f"Modelo: {modelo}, Preço: {detalhes['preço']}, Quantidade: {detalhes['quantidade']}")

# Menu interativo
def menu():
    while True:
        print("\nMenu de opções:")
        print("1. Adicionar carro")
        time.sleep(0.5)
        print("2. Excluir carro")
        time.sleep(0.5)
        print("3. Alterar preço do carro")
        time.sleep(0.5)
        print("4. Modificar quantidade de carro")
        time.sleep(0.5)
        print("5. Imprimir todo o estoque")
        time.sleep(0.5)
        print("6. Sair")
        time.sleep(0.5)
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == '1':
            adicionar_carro()
        elif opcao == '2':
            excluir_carro()
        elif opcao == '3':
            alterar_preco()
        elif opcao == '4':
            modificar_quantidade()
        elif opcao == '5':
            imprimir_estoque()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        
# Executar o menu
menu()
