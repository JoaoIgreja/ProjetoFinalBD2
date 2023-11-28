from typing import List
from database import Database
from JogadorCLI import PersonagemCLI
from JogadorDAO import JogoDAO


def main():
    personagem_model = JogoDAO(database=Database(
        database="ProjetoFinalBD2", collection="Personagem"))
    cli = PersonagemCLI(personagem_model)
    cli.run()


if __name__ == "__main__":
    main()
