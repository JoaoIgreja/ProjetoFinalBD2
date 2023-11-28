from typing import List


class Cuidador:
    def __init__(self, nome: str, nascimento: str):
        self.nome = nome
        self.nascimento = nascimento


class Habilidade:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["descricao"])


class Personagem:
    def __init__(self, nome: str, classe: str, nivel: int, habilidades: List[Habilidade]):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.habilidades = habilidades
