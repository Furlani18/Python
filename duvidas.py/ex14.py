import time

dicionario = {
    "Notebook Dell": {"Quantidade": 300, "Preço": 2700.00},
    "Notebook Lenovo": {"Quantidade": 300, "Preço": 2100.00},
    "Fone de Ouvido JBL": {"Quantidade": 300, "Preço": 250.00},
    "Caixa de Som Boombox 3 JBL": {"Quantidade": 300, "Preço": 2000.00},
    "Console PS5 Playstation": {"Quantidade": 300, "Preço": 3500.00},
    "Console Xbox X Series": {"Quantidade": 300, "Preço": 3200.00},
}

estoque = dicionario

def inserir_no_estoque(estoque):
    print("\n=== Inserir no Estoque ===")
    N = input("Insira o produto que deseja: ")
    if N in estoque:
        print("Produto já existe no estoque.")
        return
    try:
        Q = int(input("Coloque a quantidade que deseja: "))
        P = float(input("Insira o preço do produto: "))
        itens_produtos = {"Quantidade": Q, "Preço": P}
        estoque[N] = itens_produtos
        print("Produto inserido no estoque com sucesso!")
        imprimir_todo_o_estoque(estoque)  # Imprimir estoque após a inserção
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def excluir_do_estoque(estoque):
    print("\n=== Excluir do Estoque ===")
    N = input("Insira o produto que deseja excluir: ")
    if N in estoque:
        del estoque[N]
        print(f"O produto {N} foi excluído com sucesso.")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def atualizar_preço_do_estoque(estoque):
    print("\n=== Atualizar Preço do Estoque ===")
    N = input("Digite o produto que deseja alterar o preço: ")
    if N in estoque:
        try:
            P = float(input("Coloque o novo preço: "))
            estoque[N]["Preço"] = P
            print(f"O produto {N} teve seu preço alterado para {P}.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def atualizar_quantidade_do_estoque(estoque):
    print("\n=== Atualizar Quantidade do Estoque ===")
    N = input("Digite o produto que deseja alterar a quantidade: ")
    if N in estoque:
        try:
            Q = int(input("Coloque a nova quantidade que deseja: "))
            estoque[N]["Quantidade"] = Q
            print(f"O produto {N} teve sua quantidade alterada para {Q}.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def imprimir_todo_o_estoque(estoque):
    print("\n=== Estoque Atual ===")
    for nome_do_produto, detalhes in estoque.items():
        print(f"Produto: {nome_do_produto}")
        print(f"Quantidade: {detalhes['Quantidade']}")
        print(f"Preço: R${detalhes['Preço']:.2f}")
        print("-" * 30)  # Linha divisória entre os produtos

def menu():
    while True:
        print("\n" + "=" * 50)
        print("                 Sistema de Estoque")
        print("=" * 50)
        print("1. Inserir no estoque")
        print("2. Excluir do estoque")
        print("3. Atualizar preço do estoque")
        print("4. Atualizar quantidade do estoque")
        print("5. Imprimir todo o estoque")
        print("6. Sair do sistema...")
        print("=" * 50)

        escolha = input("Escolha o que deseja realizar: ")
        print("=" * 50)
        
        if escolha == "1":
            inserir_no_estoque(estoque)
        elif escolha == "2":
            excluir_do_estoque(estoque)
        elif escolha == "3":
            atualizar_preço_do_estoque(estoque)
        elif escolha == "4":
            atualizar_quantidade_do_estoque(estoque)
        elif escolha == "5":
            imprimir_todo_o_estoque(estoque)
        elif escolha == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente!!")

menu()
