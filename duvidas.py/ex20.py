import os
import json
import time

class Veiculo:
    def __init__(self, marca, modelo, ano, preco, tipo):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.tipo = tipo  # 'carro' ou 'moto'

    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - R${self.preco:.2f}"


class Estoque:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def listar_veiculos(self):
        if not self.veiculos:
            return "Estoque vazio."
        else:
            lista = "\n".join([veiculo.exibir_informacoes() for veiculo in self.veiculos])
            return f"Veículos disponíveis:\n{lista}"

    def buscar_veiculo_por_modelo(self, modelo):
        encontrados = [veiculo for veiculo in self.veiculos if veiculo.modelo.lower() == modelo.lower()]
        if encontrados:
            return encontrados
        else:
            return None

    def vender_veiculo(self, modelo):
        for veiculo in self.veiculos:
            if veiculo.modelo.lower() == modelo.lower():
                self.veiculos.remove(veiculo)
                return veiculo
        return None

    def sugerir_veiculos(self, modelo):
        sugestoes = [veiculo for veiculo in self.veiculos if modelo.lower() in veiculo.modelo.lower()]
        return sugestoes

    def calcular_lucro_total(self):
        return sum(veiculo.preco for veiculo in self.veiculos)

    def salvar_estoque(self, nome_arquivo):
        with open(nome_arquivo, 'w') as file:
            json.dump([vars(veiculo) for veiculo in self.veiculos], file)

    def carregar_estoque(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as file:
                data = json.load(file)
                self.veiculos = [Veiculo(**veiculo) for veiculo in data]


# Funções para interação com o usuário
def exibir_menu():
    print("\n===== Menu Principal =====")
    print("1. Listar veículos disponíveis")
    print("2. Adicionar veículo ao estoque")
    print("3. Buscar veículo por modelo")
    print("4. Vender veículo")
    print("5. Calcular lucro total")
    print("6. Salvar estoque em arquivo")
    print("7. Carregar estoque de arquivo")
    print("8. Sair do sistema")


def listar_veiculos_disponiveis(estoque):
    print("\n===== Veículos Disponíveis =====")
    if not estoque.veiculos:
        print("Estoque vazio.")
    else:
        for idx, veiculo in enumerate(estoque.veiculos, start=1):
            print(f"{idx}. Marca: {veiculo.marca} | Modelo: {veiculo.modelo} | Ano: {veiculo.ano} | Preço: R${veiculo.preco:.2f} | Tipo: {veiculo.tipo}")
            time.sleep(0.5)  # Atraso de 0.5 segundos entre cada veículo


def adicionar_veiculo(estoque):
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = int(input("Digite o ano do veículo: "))
    preco = float(input("Digite o preço do veículo: "))
    tipo = input("Digite o tipo do veículo (carro ou moto): ")

    veiculo = Veiculo(marca, modelo, ano, preco, tipo)
    estoque.adicionar_veiculo(veiculo)
    print(f"\nVeículo {veiculo.modelo} adicionado ao estoque.")


def buscar_veiculo_por_modelo(estoque):
    modelo = input("Digite o modelo do veículo a buscar: ")
    encontrados = estoque.buscar_veiculo_por_modelo(modelo)
    if encontrados:
        print("\nVeículos encontrados:")
        for veiculo in encontrados:
            print(veiculo.exibir_informacoes())
    else:
        print(f"\nNenhum veículo encontrado com o modelo '{modelo}'.")


def vender_veiculo(estoque):
    modelo = input("Digite o modelo do veículo a vender: ")
    veiculo_vendido = estoque.vender_veiculo(modelo)
    if veiculo_vendido:
        print(f"\nVeículo vendido:\n{veiculo_vendido.exibir_informacoes()}")
    else:
        print(f"\nVeículo {modelo} não encontrado no estoque.")
        sugeridos = estoque.sugerir_veiculos(modelo)
        if sugeridos:
            print("Talvez você esteja procurando por:")
            for veiculo in sugeridos:
                print(veiculo.exibir_informacoes())


def calcular_lucro_total(estoque):
    lucro_total = estoque.calcular_lucro_total()
    print(f"\nLucro total obtido com as vendas: R${lucro_total:.2f}")


def salvar_estoque(estoque):
    nome_arquivo = input("Digite o nome do arquivo para salvar o estoque (ex: estoque.json): ")
    estoque.salvar_estoque(nome_arquivo)
    print(f"\nEstoque salvo com sucesso no arquivo '{nome_arquivo}'.")


def carregar_estoque(estoque):
    nome_arquivo = input("Digite o nome do arquivo para carregar o estoque (ex: estoque.json): ")
    estoque.carregar_estoque(nome_arquivo)
    print(f"\nEstoque carregado com sucesso do arquivo '{nome_arquivo}'.")


# Programa principal
def main():
    estoque = Estoque()

    # Carregar estoque inicial
    estoque.carregar_estoque("estoque.json")

    while True:
        exibir_menu()

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            listar_veiculos_disponiveis(estoque)
        elif opcao == '2':
            adicionar_veiculo(estoque)
        elif opcao == '3':
            buscar_veiculo_por_modelo(estoque)
        elif opcao == '4':
            vender_veiculo(estoque)
        elif opcao == '5':
            calcular_lucro_total(estoque)
        elif opcao == '6':
            salvar_estoque(estoque)
        elif opcao == '7':
            carregar_estoque(estoque)
        elif opcao == '8':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 8.")

    print("Obrigado por usar o sistema de vendas de veículos!")


if __name__ == "__main__":
    main()
