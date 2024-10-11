import random
import json

# Lista de times participantes do Campeonato Brasileiro 2024
times = [
    "Flamengo", "Palmeiras", "Bahia", "Botafogo",
    "Athletico-PR", "Bragantino", "Internacional", "Cruzeiro",
    "São Paulo", "Atlético-MG", "Fortaleza", "Juventude",
    "Criciúma", "Cuiabá", "Vasco da Gama", "Atlético-GO",
    "Vitória", "Corinthians", "Grêmio", "Fluminense"
]

# Função para gerar as rodadas
def gerar_rodadas(times):
    rodadas = []
    random.shuffle(times)
    for i in range(len(times)-1):
        rodada = []
        for j in range(len(times)//2):
            casa = times[j]
            fora = times[-(j+1)]
            rodada.append((casa, fora))
        rodadas.append(rodada)
        times = [times[0]] + times[-1:] + times[1:-1]
    return rodadas

# Classe para gerenciar o campeonato
class Campeonato:
    def __init__(self, times):
        self.times = times
        self.pontuacao = {time: 0 for time in times}
        self.vitorias = {time: 0 for time in times}
        self.empates = {time: 0 for time in times}
        self.derrotas = {time: 0 for time in times}
        self.saldo_gols = {time: 0 for time in times}
        self.rodadas = gerar_rodadas(times)
        self.resultados = []
        self.artilheiros = {}
        self.rodada_atual = 1
    
    def registrar_resultado(self, rodada, resultados):
        if rodada < 1 or rodada > 38:
            print("Rodada inválida. Insira uma rodada entre 1 e 38.")
            return
        
        for jogo in resultados:
            time_casa, gols_casa, time_fora, gols_fora = jogo
            time_casa = time_casa.strip()  # Remove espaços extras no início e fim do nome
            time_fora = time_fora.strip()  # Remove espaços extras no início e fim do nome
            
            if time_casa not in self.times or time_fora not in self.times:
                print(f"Um dos times ({time_casa} ou {time_fora}) não está na lista de times participantes.")
                continue
            
            if gols_casa > gols_fora:
                self.pontuacao[time_casa] += 3
                self.vitorias[time_casa] += 1
                self.derrotas[time_fora] += 1
            elif gols_casa < gols_fora:
                self.pontuacao[time_fora] += 3
                self.vitorias[time_fora] += 1
                self.derrotas[time_casa] += 1
            else:
                self.pontuacao[time_casa] += 1
                self.pontuacao[time_fora] += 1
                self.empates[time_casa] += 1
                self.empates[time_fora] += 1
            
            self.saldo_gols[time_casa] += (gols_casa - gols_fora)
            self.saldo_gols[time_fora] += (gols_fora - gols_casa)
            
            self.resultados.append((rodada, time_casa, gols_casa, time_fora, gols_fora))
        
        self.rodada_atual = rodada
    
    def mostrar_classificacao(self):
        classificacao = sorted(self.pontuacao.items(), key=lambda x: (x[1], self.saldo_gols[x[0]], self.vitorias[x[0]], -self.derrotas[x[0]], -self.empates[x[0]]), reverse=True)
        print("\nClassificação:")
        print(f"{'Posição':<8}{'Time':<15}{'Pts':<5}{'V':<5}{'E':<5}{'D':<5}{'SG':<5}")
        for i, (time, pontos) in enumerate(classificacao, start=1):
            print(f"{i:<8}{time:<15}{pontos:<5}{self.vitorias[time]:<5}{self.empates[time]:<5}{self.derrotas[time]:<5}{self.saldo_gols[time]:<5}")
    
    def registrar_artilheiro(self, nome, time, gols):
        if nome in self.artilheiros:
            self.artilheiros[nome]['gols'] += gols
        else:
            self.artilheiros[nome] = {'time': time, 'gols': gols}
    
    def mostrar_artilheiros(self):
        artilheiros_ordenados = sorted(self.artilheiros.items(), key=lambda x: x[1]['gols'], reverse=True)
        print("\nArtilheiros:")
        for i, (nome, dados) in enumerate(artilheiros_ordenados, start=1):
            print(f"{i}. {nome} ({dados['time']}): {dados['gols']} gols")
    
    def salvar_dados(self, arquivo):
        dados = {
            'pontuacao': self.pontuacao,
            'vitorias': self.vitorias,
            'empates': self.empates,
            'derrotas': self.derrotas,
            'saldo_gols': self.saldo_gols,
            'resultados': self.resultados,
            'artilheiros': self.artilheiros,
            'rodada_atual': self.rodada_atual
        }
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
        print("Dados salvos com sucesso.")
    
    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
            self.pontuacao = dados['pontuacao']
            self.vitorias = dados['vitorias']
            self.empates = dados['empates']
            self.derrotas = dados['derrotas']
            self.saldo_gols = dados['saldo_gols']
            self.resultados = dados['resultados']
            self.artilheiros = dados['artilheiros']
            self.rodada_atual = dados['rodada_atual']
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo não encontrado. Iniciando novo campeonato.")
    
    def excluir_dados(self):
        opcao = input("\nVocê deseja:\n1. Excluir todos os dados do campeonato\n2. Reiniciar a partir da rodada atual\nEscolha uma opção (1 ou 2): ")
        
        if opcao == "1":
            self.pontuacao = {time: 0 for time in self.times}
            self.vitorias = {time: 0 for time in self.times}
            self.empates = {time: 0 for time in self.times}
            self.derrotas = {time: 0 for time in self.times}
            self.saldo_gols = {time: 0 for time in self.times}
            self.resultados = []
            self.artilheiros = {}
            self.rodada_atual = 1
            print("Todos os dados do campeonato foram excluídos.")
        elif opcao == "2":
            rodada = int(input("A partir de qual rodada você deseja reiniciar (1 a 38): "))
            if rodada < 1 or rodada > 38:
                print("Rodada inválida.")
                return
            self.resultados = [r for r in self.resultados if r[0] < rodada]
            self.rodada_atual = rodada
            print(f"Todos os resultados a partir da rodada {rodada} foram excluídos.")
        else:
            print("Opção inválida.")

# Inicializa o campeonato
campeonato = Campeonato(times)

# Menu de interação com o usuário
def menu():
    while True:
        print("\nMenu:")
        print("Rodada Atual:", campeonato.rodada_atual)
        print("1. Registrar resultados da rodada")
        print("2. Mostrar classificação")
        print("3. Registrar artilheiro")
        print("4. Mostrar artilheiros")
        print("5. Salvar dados")
        print("6. Carregar dados")
        print("7. Excluir dados")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            rodada = int(input("Rodada: "))
            num_jogos = int(input("Quantidade de jogos: "))
            resultados = []
            for _ in range(num_jogos):
                print(f"Jogo {_ + 1}:")
                time_casa = input("Time da casa: ")
                gols_casa = int(input("Gols da casa: "))
                time_fora = input("Time de fora: ")
                gols_fora = int(input("Gols de fora: "))
                resultados.append((time_casa, gols_casa, time_fora, gols_fora))
            campeonato.registrar_resultado(rodada, resultados)
        elif opcao == "2":
            campeonato.mostrar_classificacao()
        elif opcao == "3":
            nome = input("Nome do artilheiro: ")
            time = input("Time do artilheiro: ")
            gols = int(input("Número de gols: "))
            campeonato.registrar_artilheiro(nome, time, gols)
        elif opcao == "4":
            campeonato.mostrar_artilheiros()
        elif opcao == "5":
            arquivo = input("Nome do arquivo para salvar (com extensão .json): ")
            campeonato.salvar_dados(arquivo)
        elif opcao == "6":
            arquivo = input("Nome do arquivo para carregar (com extensão .json): ")
            campeonato.carregar_dados(arquivo)
        elif opcao == "7":
            campeonato.excluir_dados()
        elif opcao == "8":
            break
        else:
            print("Opção inválida!")

menu()
