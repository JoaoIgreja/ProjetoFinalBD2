from classes import Cuidador, Habilidade, Personagem

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PersonagemCLI(SimpleCLI):
    def __init__(self, jogoDAO):
        super().__init__()
        self.jogoDAO = jogoDAO
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update_personagem)
        self.add_command("delete", self.delete)

    def create(self):
        print("Seja muito bem-vindo jogador!!")
        nome = input("Qual o seu nome? ")
        nascimento = input(f"Qual o seu nascimento, {nome}? ")
        jogador = Cuidador(nome, nascimento)

        habilidades = []
        quant = int(input("Quantas habilidades você quer criar? "))
        for i in range(0, quant):
            nome_habilidade = input("Qual o nome da habilidade? ")
            descricao_habilidade = input("Descreva a habilidade: ")
            habilidade = Habilidade(nome_habilidade, descricao_habilidade)
            habilidades.append(habilidade.to_dict())  # Convertendo a habilidade em dicionário

        nome_personagem = input(f"Qual o nome do personagem? ")
        classe_personagem = input(f"Qual a classe do personagem? ")
        nivel_personagem = int(input(f"Qual o nível do personagem? "))

        self.jogoDAO.create_personagem(nome_personagem, classe_personagem, nivel_personagem, habilidades)

    def read(self):
        print(f"Digite o ID do personagem: ")
        id = str(input())
        self.jogoDAO.read_personagem_by_id(id)

    def update_personagem(self):
        print(f"Digite o ID do personagem: ")
        id = str(input())
        nome = input(f"Digite o novo nome do personagem: ")
        self.jogoDAO.update_personagem(id, nome)

    def delete(self):
        print(f"Digite o ID do personagem: ")
        id = str(input())
        self.jogoDAO.delete_personagem(id)