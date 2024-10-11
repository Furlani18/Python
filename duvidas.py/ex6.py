dicionario = {
    "maça": {"Quantidade": 100, "Preco": 1.5},
    "abacaxi": {"Quantidade": 100, "Preco": 2.7},
    "banana": {"Quantidade": 100, "Preco": 3.2},
}

def inserir_no_estoque(estoque):
    N = input("Digite o nome do produto: ")
    Q = int(input("Quantidade disponível: "))
    P = float(input("Digite o preço do produto: "))
    itens_produtos = {"Quantidade": Q, "Preco": P}
    estoque[N] = itens_produtos
    print(estoque)

def excluir_do_estoque(estoque):
    N = input("Digite o nome do produto a ser excluído: ")
    if N in estoque:
        del estoque[N]
        print(f"Produto {N} excluído do estoque.")
    else:
        print(f"Produto {N} não encontrado no estoque.")

def modificar_preco_do_estoque(estoque):
    N = input("Digite o produto para alteração de preço: ")
    P = float(input("Novo preço: "))
    if N in estoque:
        estoque[N]["Preco"] = P
        print(f"Preço do produto {N} alterado para {P}.")
    else:
        print(f"Produto {N} não encontrado no estoque.")

def modificar_quantidade_do_estoque(estoque):
    N = input("Digite o nome do produto a ser modificado: ")
    Q = int(input("Quantidade a ser modificada: "))
    if N in estoque:
        estoque[N]["Quantidade"] = Q
        print(f"Quantidade do produto {N} alterada para {Q}.")
    else:
        print(f"Produto {N} não encontrado no estoque.")

def imprimir_todo_o_estoque(estoque):
    for nome_do_produto, detalhes in estoque.items():
        print(f"Produto: {nome_do_produto}")
        print(f"  Quantidade: {detalhes['Quantidade']}")
        print(f"  Preço: {detalhes['Preco']}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir no estoque")
        print("2. Excluir do estoque")
        print("3. Modificar preço do estoque")
        print("4. Modificar quantidade do estoque")
        print("5. Imprimir todo o estoque")
        print("6. Sair")
        
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
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
 
