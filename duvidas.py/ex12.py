import time

dicionario = {
    "Notebook Dell": {"Quantidade": 300, "Preço": 2700.00, "Endereço": "Prateleira 1"},
    "Notebook Lenovo": {"Quantidade": 300, "Preço": 2100.00,  "Endereço": "Prateleira 2"},
    "Fone de Ouvido JBL": {"Quantidade": 300, "Preço": 250.00,  "Endereço": "Prateleira 3"},
    "Caixa de Som Boombox 3 JBL": {"Quantidade": 300, "Preço": 2000.00,  "Endereço": "Prateleira 4"},
    "Console PS5 Playstation": {"Quantidade": 300, "Preço": 3500.00,  "Endereço": "Prateleira 5"},
    "Console Xbox X Series": {"Quantidade": 300, "Preço": 3200.00,  "Endereço": "Prateleira 6"},
}

def inserir_no_estoque(estoque):
    N = input("Insira o produto que deseja: ")
    Q = int(input("Coloque a quantidade que deseja: "))
    P = float(input("Insira o preço do produto: "))
    E = input("Colouque o endereço a seguir: ")
    itens_produtos = {"Quantidade": Q, "Preço": P, "Endereço": E}
    estoque[N] = itens_produtos
    print("Produto inserido no estoque com sucesso!")
    print(estoque)

def excluir_do_estoque(estoque):
    N = input("Insira o produto que deseja excluir: ")
    if N in estoque:
        del estoque[N]
        print(f"O produto {N} foi excluído com sucesso.")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def atualizar_preço_do_estoque(estoque):
    N = input("Digite o produto que deseja alterar o preço: ")
    P = float(input("Coloque o novo preço: "))
    E =  input("Insira o endereço do produto que deseja alterar: ")
    if N in estoque:
        estoque[N]["Preço"] = P
        estoque[N]["Endereço"] = E
        print(f"O produto {N} teve seu preço e seu endereço alterado para {P} e {E}")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def atualizar_quantidade_do_estoque(estoque):
    N = input("Digite o produto que deseja alterar a quantidade: ")
    Q = int(input("Coloque a nova quantidade que deseja: "))
    if N in estoque:
        estoque[N]["Quantidade"] = Q
        print(f"O produto {N} teve sua quantidade alterada para {Q}.")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def localizar_endereço_no_estoque(estoque):
    N = input("Digite o produto que deseja a seguir: ")
    E = input("Insira o endereço do produto: ")
    if N in estoque:
        estoque[N]["Endereço"] = E
        print(f"O produto {N} foi localizado no {E}")
    else:
        print(f"O produto {N} não foi encontrado no estoque.")

def imprimir_todo_o_estoque(estoque):
    for nome_do_produto, detalhes in estoque.items():
        print(f"Produto: {nome_do_produto}")
        print(f"Quantidade: {detalhes['Quantidade']}")
        print(f"Preço: {detalhes['Preço']}")
        print(f"Endereço: {detalhes['Endereço']}")
        print()  # Linha em branco para separar os produtos
        

def menu():
    while True:
        print("\nMenu: ")
        print("1. Inserir no estoque")
        time.sleep(0.75)
        print("2. Excluir do estoque")
        time.sleep(0.75)
        print("3. Atualizar preço do estoque")
        time.sleep(0.75)
        print("4. Atualizar quantidade do estoque")
        time.sleep(0.75)
        print("5. Imprimir todo o estoque")
        time.sleep(0.75)
        print("6. Localize o endereço do produto")
        time.sleep(0.75)
        print("7. Sair do estoque...")
        time.sleep(0.75)

        escolha = input("Escolha o que deseja realizar: ")
        if escolha == "1":
            inserir_no_estoque(dicionario)
        elif escolha == "2":
            excluir_do_estoque(dicionario)
        elif escolha == "3":
            atualizar_preço_do_estoque(dicionario)
        elif escolha == "4":
            atualizar_quantidade_do_estoque(dicionario)
        elif escolha == "5":
            imprimir_todo_o_estoque(dicionario)
        elif escolha == "6":
            localizar_endereço_no_estoque(dicionario)
        elif escolha == "7":
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida, tente novamente")
menu()



# elif escolha == "6":
    # print("Saindo do sistema...")
    # break
# else:
    # print("Opção inválida, tente novamente!!")