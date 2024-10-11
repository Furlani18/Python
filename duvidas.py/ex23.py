import os
import json
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Veiculo:
    def __init__(self, marca, modelo, ano, preco, tipo, vendido=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.tipo = tipo  
        self.vendido = vendido  

    def exibir_informacoes(self):
        status = "Vendido" if self.vendido else "Disponível"
        return f"{self.marca} {self.modelo} ({self.ano}) - R${self.preco:.2f} - Tipo: {self.tipo} - Status: {status}"

    def to_dict(self):
        return {
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'preco': self.preco,
            'tipo': self.tipo,
            'vendido': self.vendido
        }

class Estoque:
    def __init__(self):
        self.veiculos = []
        self.veiculos_vendidos = [] 
        self.log_acoes = []  

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        self.log_acoes.append(f"Veículo {veiculo.modelo} adicionado ao estoque.")

    def listar_veiculos(self):
        if not self.veiculos:
            return "Estoque vazio."
        else:
            lista = "\n".join([veiculo.exibir_informacoes() for veiculo in self.veiculos if not veiculo.vendido])
            return f"Veículos disponíveis:\n{lista}"

    def listar_veiculos_vendidos(self):
        if not self.veiculos_vendidos:
            return "Nenhum veículo vendido."
        else:
            lista = "\n".join([veiculo.exibir_informacoes() for veiculo in self.veiculos_vendidos])
            return f"Veículos vendidos:\n{lista}"

    def buscar_veiculo_por_modelo(self, modelo):
        encontrados = [veiculo for veiculo in self.veiculos if veiculo.modelo.lower() == modelo.lower() and not veiculo.vendido]
        if encontrados:
            return encontrados
        else:
            return None

    def vender_veiculo(self, modelo):
        for idx, veiculo in enumerate(self.veiculos):
            if veiculo.modelo.lower() == modelo.lower() and not veiculo.vendido:
                veiculo.vendido = True
                self.veiculos_vendidos.append(veiculo)
                self.log_acoes.append(f"Veículo {veiculo.modelo} vendido.")

               
                self.salvar_historico_vendas()

                
                if idx + 1 < len(self.veiculos):
                    proximo_veiculo = self.veiculos[idx + 1]
                    print(Fore.GREEN + f"\nPróximo veículo disponível:\n{proximo_veiculo.exibir_informacoes()}")

                return veiculo
        return None

    def sugerir_veiculos(self, modelo):
        sugestoes = [veiculo for veiculo in self.veiculos if modelo.lower() in veiculo.modelo.lower() and not veiculo.vendido]
        return sugestoes

    def calcular_lucro_total(self):
        lucro_total = sum(veiculo.preco for veiculo in self.veiculos_vendidos)
        return lucro_total

    def aplicar_desconto(self, modelo, percentual_desconto):
        for veiculo in self.veiculos:
            if veiculo.modelo.lower() == modelo.lower() and not veiculo.vendido:
                veiculo.preco *= (1 - percentual_desconto / 100)
                self.log_acoes.append(f"Desconto de {percentual_desconto}% aplicado no veículo {veiculo.modelo}.")
                return veiculo
        return None

    def salvar_estoque(self, nome_arquivo):
        with open(nome_arquivo, 'w') as file:
            json.dump([veiculo.to_dict() for veiculo in self.veiculos], file, indent=4)
        self.log_acoes.append(f"Estoque salvo no arquivo '{nome_arquivo}'.")

    def carregar_estoque(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as file:
                data = json.load(file)
                self.veiculos = [Veiculo(**veiculo) for veiculo in data]
            self.log_acoes.append(f"Estoque carregado do arquivo '{nome_arquivo}'.")

    def salvar_historico_vendas(self):
        with open("historico_vendas.json", 'w') as file:
            json.dump([veiculo.to_dict() for veiculo in self.veiculos_vendidos], file, indent=4)

    def salvar_log_acoes(self):
        with open("log_acoes.txt", 'w') as file:
            for acao in self.log_acoes:
                file.write(f"{acao}\n")

    def backup_estoque(self):
        nome_arquivo_backup = f"backup_estoque_{time.strftime('%Y%m%d_%H%M%S')}.json"
        self.salvar_estoque(nome_arquivo_backup)
        print(Fore.GREEN + f"\nBackup do estoque salvo com sucesso no arquivo '{nome_arquivo_backup}' 📦")

def exibir_menu():
    print(Fore.CYAN + "\n===== Menu Principal =====")
    print(Fore.GREEN + "1. Listar veículos disponíveis 🚗")
    print(Fore.GREEN + "2. Adicionar veículo ao estoque ➕")
    print(Fore.GREEN + "3. Buscar veículo por modelo 🔍")
    print(Fore.GREEN + "4. Vender veículo 🛠️")
    print(Fore.GREEN + "5. Calcular lucro total 💰")
    print(Fore.GREEN + "6. Listar veículos vendidos 📜")
    print(Fore.GREEN + "7. Aplicar desconto em veículo 🤑")
    print(Fore.GREEN + "8. Salvar estoque em arquivo 💾")
    print(Fore.GREEN + "9. Carregar estoque de arquivo 📂")
    print(Fore.GREEN + "10. Fazer backup do estoque 📦")
    print(Fore.RED + "11. Sair do sistema 🚪")

def listar_veiculos_disponiveis(estoque):
    print(Fore.CYAN + "\n===== Veículos Disponíveis =====")
    if not estoque.veiculos:
        print(Fore.RED + "Estoque vazio.")
    else:
        for idx, veiculo in enumerate(estoque.veiculos, start=1):
            if not veiculo.vendido:
                print(Fore.WHITE + f"{idx}. {veiculo.exibir_informacoes()}")
            time.sleep(0.5)  

def adicionar_veiculo(estoque):
    print(Fore.CYAN + "\n===== Adicionar Veículo ao Estoque =====")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    while True:
        try:
            ano = int(input("Digite o ano do veículo: "))
            if ano <= 0:
                raise ValueError("Ano deve ser um número inteiro positivo.")
            break
        except ValueError as e:
            print(Fore.RED + f"Erro: {e}")
    while True:
        try:
            preco = float(input("Digite o preço do veículo: "))
            if preco <= 0:
                raise ValueError("Preço deve ser um número positivo.")
            break
        except ValueError as e:
            print(Fore.RED + f"Erro: {e}")
    tipo = input("Digite o tipo do veículo (carro, moto, caminhonete, SUV, Off-Road, esportivos): ")

    veiculo = Veiculo(marca, modelo, ano, preco, tipo)
    estoque.adicionar_veiculo(veiculo)
    print(Fore.GREEN + f"\nVeículo {veiculo.modelo} adicionado ao estoque com sucesso! ✅")

def buscar_veiculo_por_modelo(estoque):
    print(Fore.CYAN + "\n===== Buscar Veículo por Modelo =====")
    modelo = input("Digite o modelo do veículo a buscar: ")
    encontrados = estoque.buscar_veiculo_por_modelo(modelo)
    if encontrados:
        print(Fore.CYAN + "\nVeículos encontrados:")
        for veiculo in encontrados:
            print(Fore.YELLOW + veiculo.exibir_informacoes())
    else:
        print(Fore.RED + f"\nNenhum veículo encontrado com o modelo '{modelo}'.")
        sugerir_veiculos(estoque, modelo)

def vender_veiculo(estoque):
    print(Fore.CYAN + "\n===== Vender Veículo =====")
    modelo = input("Digite o modelo do veículo a vender: ")
    veiculo = estoque.vender_veiculo(modelo)
    if veiculo:
        print(Fore.GREEN + f"\nVeículo {veiculo.modelo} vendido com sucesso! 🛠️")
    else:
        print(Fore.RED + f"\nNenhum veículo disponível com o modelo '{modelo}' encontrado.")

def sugerir_veiculos(estoque, modelo):
    sugestoes = estoque.sugerir_veiculos(modelo)
    if sugestoes:
        print(Fore.CYAN + "\nSugestões de veículos similares:")
        for veiculo in sugestoes:
            print(Fore.YELLOW + veiculo.exibir_informacoes())
    else:
        print(Fore.RED + "\nNenhuma sugestão disponível.")

def calcular_lucro_total(estoque):
    lucro_total = estoque.calcular_lucro_total()
    print(Fore.GREEN + f"\nLucro total com veículos vendidos: R${lucro_total:.2f} 💰")

def listar_veiculos_vendidos(estoque):
    print(Fore.CYAN + "\n===== Veículos Vendidos =====")
    if not estoque.veiculos_vendidos:
        print(Fore.RED + "Nenhum veículo vendido.")
    else:
        for idx, veiculo in enumerate(estoque.veiculos_vendidos, start=1):
            print(Fore.YELLOW + f"{idx}. {veiculo.exibir_informacoes()}")

def aplicar_desconto(estoque):
    print(Fore.CYAN + "\n===== Aplicar Desconto =====")
    modelo = input("Digite o modelo do veículo para aplicar desconto: ")
    while True:
        try:
            percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
            if percentual_desconto <= 0 or percentual_desconto >= 100:
                raise ValueError("Percentual de desconto deve ser um número positivo entre 0 e 100.")
            break
        except ValueError as e:
            print(Fore.RED + f"Erro: {e}")
    veiculo = estoque.aplicar_desconto(modelo, percentual_desconto)
    if veiculo:
        print(Fore.GREEN + f"\nDesconto de {percentual_desconto}% aplicado ao veículo {veiculo.modelo} com sucesso! 🤑")
    else:
        print(Fore.RED + f"\nNenhum veículo disponível com o modelo '{modelo}' encontrado.")

def salvar_estoque(estoque):
    print(Fore.CYAN + "\n===== Salvar Estoque =====")
    nome_arquivo = input("Digite o nome do arquivo para salvar o estoque: ")
    estoque.salvar_estoque(nome_arquivo)
    print(Fore.GREEN + f"\nEstoque salvo com sucesso no arquivo '{nome_arquivo}' 💾")

def carregar_estoque(estoque):
    print(Fore.CYAN + "\n===== Carregar Estoque =====")
    nome_arquivo = input("Digite o nome do arquivo para carregar o estoque: ")
    estoque.carregar_estoque(nome_arquivo)
    print(Fore.GREEN + f"\nEstoque carregado com sucesso do arquivo '{nome_arquivo}' 📂")

def backup_estoque(estoque):
    print(Fore.CYAN + "\n===== Backup do Estoque =====")
    estoque.backup_estoque()

def main():
    estoque = Estoque()
    while True:
        exibir_menu()
        escolha = input(Fore.YELLOW + "Escolha uma opção: ")
        if escolha == '1':
            listar_veiculos_disponiveis(estoque)
        elif escolha == '2':
            adicionar_veiculo(estoque)
        elif escolha == '3':
            buscar_veiculo_por_modelo(estoque)
        elif escolha == '4':
            vender_veiculo(estoque)
        elif escolha == '5':
            calcular_lucro_total(estoque)
        elif escolha == '6':
            listar_veiculos_vendidos(estoque)
        elif escolha == '7':
            aplicar_desconto(estoque)
        elif escolha == '8':
            salvar_estoque(estoque)
        elif escolha == '9':
            carregar_estoque(estoque)
        elif escolha == '10':
            backup_estoque(estoque)
        elif escolha == '11':
            print(Fore.CYAN + "Saindo do sistema. Obrigado por utiizar o nosso site. Até mais! 🚪")
            estoque.salvar_log_acoes()
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()