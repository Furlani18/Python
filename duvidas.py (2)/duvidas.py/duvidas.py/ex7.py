import time

dicionario = {
    "maçã": {"Quantidade": 100, "Preço": 1.5},
    "Pera": {"Quantidade": 100, "Preço": 2.2},
    "Abacaxi": {"Quantidade": 100, "Preço": 3.1},
    "Melancia": {"Quantidade": 100, "Preço": 4.5}
}

def inserir_no_estoque(estoque):
    N = input("Digite o nome do produto: ")
    Q = int(input("Insira a quantidade: "))
    P = float(input("Coloque o preço do produto: "))
    itens_produtos = {"Quantidade": Q, "Preço": P}
    estoque[N] = itens_produtos
    print(estoque)

def excluir_do_estoque(estoque):
    N = input("Digite o nome do produto que deseja excluir: ")
    if N in estoque:
        del estoque[N]
        print(f"Produto {N} excluído com sucesso")
    else:
        print(f"Produto {N} não foi encontrado!")

def modificar_preco_do_estoque(estoque):
    N = input("Digite o produto para alteração de preço: ")
    P = float(input("Novo preço: "))
    if N in estoque:
        estoque[N]["Preço"] = P
        print(f"Preço do produto {N} alterado para {P}.")
    else:
        print(f"Produto {N} não encontrado no estoque.")

def modificar_quantidade_do_estoque(estoque):
    N = input("Digite o produto que deseja modificar a quantidade: ")
    Q = int(input("Digite a nova quantidade: "))
    if N in estoque:
        estoque[N]["Quantidade"] = Q
        print(f"A quantidade do produto {N} foi alterada para {Q}.")
    else:
        print(f"Produto {N} não encontrado no estoque.")

def imprimir_todo_o_estoque(estoque):
    for nome_do_produto, detalhes in estoque.items():
        print(f"Produto: {nome_do_produto}")
        print(f"Quantidade: {detalhes['Quantidade']}")
        print(f"Preço: {detalhes['Preço']}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir no estoque")
        time.sleep(0.5)
        print("2. Excluir do estoque")
        time.sleep(0.5)
        print("3. Modificar preço do estoque")
        time.sleep(0.5)
        print("4. Modificar quantidade do estoque")
        time.sleep(0.5)
        print("5. Imprimir todo o estoque")
        time.sleep(0.5)
        print("6. Saindo do estoque...")
        time.sleep(0.5)
        
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            inserir_no_estoque(dicionario)
        elif escolha == "2":
            excluir_do_estoque(dicionario)
        elif escolha == "3":
            modificar_preco_do_estoque(dicionario)
        elif escolha == "4":
            modificar_quantidade_do_estoque(dicionario)
        elif escolha == "5":
            imprimir_todo_o_estoque(dicionario)
        elif escolha == "6":
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida, tente novamente...")

menu()
