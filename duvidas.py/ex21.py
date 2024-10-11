class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 1000  # Saldo inicial fictício
        self.wallet = 0  # Total ganho com apostas
        self.transaction_history = []  # Histórico de transações

    def __str__(self):
        return f"Username: {self.username}, Balance: {self.balance}, Wallet: {self.wallet}"

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Depósito de {amount}. Novo saldo: {self.balance}")

    def add_to_wallet(self, amount):
        self.wallet += amount
        self.transaction_history.append(f"Ganho de aposta de {amount}. Novo total na carteira: {self.wallet}")

    def transfer_to_wallet(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.wallet += amount
            self.transaction_history.append(f"Transferência de saldo para carteira: {amount}. Novo saldo: {self.balance}, Novo total na carteira: {self.wallet}")
            return True
        return False

    def receive_transfer(self, amount):
        self.wallet += amount
        self.transaction_history.append(f"Recebimento de transferência: {amount}. Novo total na carteira: {self.wallet}")

    def place_bet_transaction(self, amount, win_amount, success):
        if success:
            self.transaction_history.append(f"Aposta de {amount} realizada. Ganho: {win_amount}. Novo total na carteira: {self.wallet}")
        else:
            self.transaction_history.append(f"Aposta de {amount} realizada e perdida. Saldo restante: {self.balance}")

    def transfer_transaction(self, receiver_username, amount):
        self.transaction_history.append(f"Transferência de {amount} para {receiver_username}. Novo saldo: {self.balance}")

    def view_transaction_history(self):
        return "\n".join(self.transaction_history)


class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            return True
        return False

    def authenticate(self, username, password):
        if username in self.users:
            return self.users[username].password == password
        return False

    def get_user(self, username):
        return self.users.get(username)

    def transfer_balance(self, sender_username, receiver_username, amount):
        sender = self.get_user(sender_username)
        receiver = self.get_user(receiver_username)
        if sender and receiver and sender.transfer_to_wallet(amount):
            receiver.receive_transfer(amount)
            sender.transfer_transaction(receiver_username, amount)
            return True
        return False

    def list_users(self):
        return self.users.keys()


class Event:
    def __init__(self, event_name, teams, date):
        self.event_name = event_name
        self.teams = teams
        self.date = date
        self.bets = {}  # Dicionário para armazenar tipos de apostas e odds

    def add_bet(self, bet_type, odds):
        self.bets[bet_type] = odds


class EventDatabase:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name, teams, date):
        if event_name not in self.events:
            self.events[event_name] = Event(event_name, teams, date)
            return True
        return False

    def get_event(self, event_name):
        # Procura por eventos que contenham o nome fornecido
        for key in self.events:
            if event_name.lower() in key.lower():
                return self.events[key]
        return None


class BettingSystem:
    def __init__(self, user_db, event_db):
        self.user_db = user_db
        self.event_db = event_db

    def place_bet(self, username, event_name, bet_type, amount):
        user = self.user_db.get_user(username)
        event = self.event_db.get_event(event_name)

        if user and event and bet_type in event.bets:
            odds = event.bets[bet_type]
            if user.balance >= amount:
                # Simplesmente reduzir o saldo do usuário para simular a aposta
                user.balance -= amount
                # Calcular o ganho da aposta e adicionar ao wallet se a aposta for bem-sucedida
                if self.simulate_bet(odds):
                    win_amount = amount * odds
                    user.add_to_wallet(win_amount)
                    user.place_bet_transaction(amount, win_amount, True)
                    return True, win_amount
                else:
                    user.place_bet_transaction(amount, 0, False)
                    return False, 0  # Aposta perdida
            else:
                return False, 0  # Saldo insuficiente
        else:
            return False, 0  # Aposta inválida

    def simulate_bet(self, odds):
        import random
        return random.random() < 1 / odds


# Função para listar eventos disponíveis
def list_events(event_db):
    print("Eventos Disponíveis:")
    for event_name in event_db.events:
        print(f"- {event_name}")


# Função para listar tipos de apostas disponíveis para um evento
def list_bets(event_db, event_name):
    event = event_db.get_event(event_name)
    if event:
        print(f"Tipos de Apostas para '{event.event_name}':")
        for bet_type, odds in event.bets.items():
            print(f"- {bet_type}: Odds {odds}")
    else:
        print(f"Evento '{event_name}' não encontrado.")


# Função para registrar um novo usuário
def register_user(user_db):
    while True:
        username = input("Digite um username: ")
        password = input("Digite uma senha: ")
        confirm_password = input("Confirme sua senha: ")

        if password != confirm_password:
            print("Senhas não coincidem. Tente novamente.")
        else:
            if user_db.add_user(username, password):
                print("Usuário registrado com sucesso!")
                return username
            else:
                print("Username já está em uso. Escolha outro username.")


# Função para realizar um depósito de saldo
def deposit_balance(user_db):
    username = input("Digite seu username para realizar o depósito: ")
    user = user_db.get_user(username)
    if user:
        amount = float(input("Digite o valor que deseja depositar: "))
        user.deposit(amount)
        print(f"Depósito de {amount} realizado com sucesso! Novo saldo: {user.balance}")
    else:
        print("Usuário não encontrado.")


# Função para transferir saldo para outra carteira
def transfer_balance(user_db):
    sender_username = input("Digite seu username: ")
    password = input("Digite sua senha: ")
    if user_db.authenticate(sender_username, password):
        receiver_username = input("Digite o username do destinatário: ")
        amount = float(input("Digite o valor que deseja transferir: "))
        if user_db.transfer_balance(sender_username, receiver_username, amount):
            print(f"Transferência de {amount} realizada com sucesso de {sender_username} para {receiver_username}!")
        else:
            print("Falha na transferência. Verifique os usernames e o saldo disponível.")
    else:
        print("Autenticação falhou. Username ou senha incorretos.")


# Função para visualizar o extrato de transações
def view_transaction_history(user_db):
    username = input("Digite seu username para ver o extrato: ")
    password = input("Digite sua senha: ")
    if user_db.authenticate(username, password):
        user = user_db.get_user(username)
        print(f"Extrato de transações para {username}:")
        print(user.view_transaction_history())
    else:
        print("Autenticação falhou. Username ou senha incorretos.")


# Função para listar todos os usuários
def list_users(user_db):
    print("Lista de Usuários:")
    for username in user_db.list_users():
        print(f"- {username}")


# Exemplo de uso do sistema de apostas interativo
if __name__ == "__main__":
    # Criar instâncias dos bancos de dados
    user_db = UserDatabase()
    event_db = EventDatabase()

    # Adicionar eventos de exemplo com tipos de apostas e odds variadas
    event_db.add_event("Futebol: Brasil x Argentina", ["Brasil", "Argentina"], "2024-07-01")
    event_db.get_event("Futebol: Brasil x Argentina").add_bet("Vencedor", 1.8)
    event_db.get_event("Futebol: Brasil x Argentina").add_bet("Mais de 2.5 gols", 2.1)
    event_db.get_event("Futebol: Brasil x Argentina").add_bet("Menos de 2.5 gols", 1.9)

    event_db.add_event("Basquete: Lakers x Celtics", ["Lakers", "Celtics"], "2024-07-02")
    event_db.get_event("Basquete: Lakers x Celtics").add_bet("Vencedor", 2.0)
    event_db.get_event("Basquete: Lakers x Celtics").add_bet("Mais de 200 pontos", 1.7)
    event_db.get_event("Basquete: Lakers x Celtics").add_bet("Menos de 200 pontos", 2.2)

    event_db.add_event("Tênis: Federer x Nadal", ["Federer", "Nadal"], "2024-07-03")
    event_db.get_event("Tênis: Federer x Nadal").add_bet("Vencedor", 1.5)
    event_db.get_event("Tênis: Federer x Nadal").add_bet("Mais de 3 sets", 2.3)
    event_db.get_event("Tênis: Federer x Nadal").add_bet("Menos de 3 sets", 1.8)

    event_db.add_event("Futebol: Itália x Inglaterra", ["Itália", "Inglaterra"], "2024-07-04")
    event_db.get_event("Futebol: Itália x Inglaterra").add_bet("Vencedor", 2.5)
    event_db.get_event("Futebol: Itália x Inglaterra").add_bet("Mais de 2.5 gols", 2.0)
    event_db.get_event("Futebol: Itália x Inglaterra").add_bet("Menos de 2.5 gols", 1.7)

    # Sistema de apostas
    betting_system = BettingSystem(user_db, event_db)

    # Simulação de interação do usuário
    while True:
        print("\n### Sistema de Apostas Esportivas ###")
        print("1. Registrar Novo Usuário")
        print("2. Depositar Saldo")
        print("3. Listar Eventos Disponíveis")
        print("4. Fazer uma Aposta")
        print("5. Ver Saldo e Carteira")
        print("6. Transferir Saldo")
        print("7. Ver Extrato de Transações")
        print("8. Listar Usuários")
        print("9. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            username = register_user(user_db)
            print(f"Bem-vindo, {username}!")
        elif choice == "2":
            deposit_balance(user_db)
        elif choice == "3":
            list_events(event_db)
        elif choice == "4":
            username = input("Digite seu username: ")
            password = input("Digite sua senha: ")

            if user_db.authenticate(username, password):
                list_events(event_db)
                event_name = input("Digite parte do nome do evento que deseja apostar: ")
                event = event_db.get_event(event_name)
                if event:
                    list_bets(event_db, event.event_name)
                    bet_type = input("Digite o tipo de aposta que deseja fazer: ")
                    amount = float(input("Digite o valor da aposta: "))

                    success, win_amount = betting_system.place_bet(username, event.event_name, bet_type, amount)

                    if success:
                        print(f"Aposta feita com sucesso! Ganho: {win_amount}")
                        print(f"Novo saldo de {username}: {user_db.get_user(username).balance}")
                        print(f"Carteira de ganhos de {username}: {user_db.get_user(username).wallet}")
                    else:
                        print("Aposta não realizada.")
                else:
                    print(f"Evento '{event_name}' não encontrado.")
            else:
                print("Login falhou. Username ou senha incorretos.")
        elif choice == "5":
            username = input("Digite seu username para ver o saldo e carteira: ")
            user = user_db.get_user(username)
            if user:
                print(f"Saldo de {username}: {user.balance}")
                print(f"Carteira de ganhos de {username}: {user.wallet}")
            else:
                print("Usuário não encontrado.")
        elif choice == "6":
            transfer_balance(user_db)
        elif choice == "7":
            view_transaction_history(user_db)
        elif choice == "8":
            list_users(user_db)
        elif choice == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")
