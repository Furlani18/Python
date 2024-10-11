import time

dicionario = {
    "Arroz": {"Quantidade": 200, "Preço": 29.9},
    "Feijão": {"Quantidade": 200, "Preço": 20.7},
    "Macarrão": {"Quantidade": 200, "Preço": 15.5},
    "Picanha": {"Quantidade": 200, "Preço": 49.90},
    "Filé de Frango": {"Quantidade": 200, "Preço": 22.5},
    "Camarão": {"Quantidade": 200, "Preço": 89.9},
    "Tilápia": {"Quantidade": 200, "Preço": 65.9},
    "Sub-zero Antártica": {"Quantidade": 200, "Preço": 2.79},
    "Coca-Cola": {"Quantidade": 200, "Preço": 3.8},
    "Heiniken": {"Quantidade": 200, "Preço": 5.5},
    "Corote": {"Quantidade": 200, "Preço": 1.0}
}

def inserir_no_estoque(estoque):
    N = input("Digite o nome do produto: ")
    Q = int(input("Digite a quantidade: "))
    P = float(input("Digite o preço: "))
    itens_produtos = {"Quantidade": Q, "Preço": P}
    estoque[N] = itens_produtos
    print(f"O produto {N} foi inserido com sucesso no estoque.\n")

def excluir_do_estoque(estoque):
    N = input("Digite o nome do produto a ser excluído: ")
    if N in estoque:
        del estoque[N]
        print(f"O produto {N} foi excluído com sucesso.\n")
    else:
        print(f"O produto {N} não foi localizado no estoque!\n")

def modificar_quantidade_do_estoque(estoque):
    N = input("Digite o nome do produto que deseja modificar a quantidade: ")
    Q = int(input("Digite a nova quantidade: "))
    if N in estoque:
        estoque[N]["Quantidade"] = Q
        print(f"A quantidade do produto {N} foi alterada para {Q}.\n")
    else:
        print(f"O produto {N} não foi localizado no estoque!\n")

def modificar_preço_do_estoque(estoque):
    N = input("Digite o produto que deseja alterar o preço: ")
    P = float(input("Altere o preço para: "))
    if N in estoque:
        estoque[N]["Preço"] = P
        print(f"O preço do produto {N} foi alterado para {P}.\n")
    else:
        print(f"O produto {N} não foi localizado no estoque!\n")

def imprimir_todo_estoque(estoque):
    print("\nEstoque Atual:\n")
    print("+" + "-"*30 + "+" + "-"*12 + "+" + "-"*10 + "+")
    print(f"| {'Produto':<28} | {'Quantidade':<10} | {'Preço':<8} |")
    print("+" + "-"*30 + "+" + "-"*12 + "+" + "-"*10 + "+")
    for nome_do_produto, detalhes in estoque.items():
        print(f"| {nome_do_produto:<28} | {detalhes['Quantidade']:<10} | R${detalhes['Preço']:<8} |")
    print("+" + "-"*30 + "+" + "-"*12 + "+" + "-"*10 + "+")

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir no estoque")
        time.sleep(0.75)
        print("2. Excluir do estoque")
        time.sleep(0.75)
        print("3. Modificar quantidade do estoque")
        time.sleep(0.75)
        print("4. Modificar preço do estoque")
        time.sleep(0.75)
        print("5. Imprimir todo o estoque")
        time.sleep(0.75)
        print("6. Saindo do sistema...")
        time.sleep(0.75)

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            inserir_no_estoque(dicionario)
        elif escolha == "2":
            excluir_do_estoque(dicionario)
        elif escolha == "3":
            modificar_quantidade_do_estoque(dicionario)
        elif escolha == "4":
            modificar_preço_do_estoque(dicionario)
        elif escolha == "5":
            imprimir_todo_estoque(dicionario)
        elif escolha == "6":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, tente novamente!!!")

menu()
