from typing import List
from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import Habilidade

class JogoDAO:
    def __init__(self, database):
        self.db = database

    def create_personagem(self, nome: str, classe: str, nivel: int, habilidades: List[Habilidade]) -> str:
        try:
            result = self.db.collection.insert_one({"nome": nome, "classe": classe, "nivel": nivel, "habilidades": habilidades})
            personagem_id = str(result.inserted_id)
            print(f"Personagem {nome} criado com o id: {personagem_id}")
            return personagem_id
        except Exception as error:
            print(f"Ocorreu um erro ao criar o personagem: {error}")
            return None

    def read_personagem_by_id(self, personagem_id: str) -> dict:
        try:
            personagem = self.db.collection.find_one({"_id": ObjectId(personagem_id)})
            if personagem:
                print(f"Personagem encontrado: {personagem}")
                return personagem
            else:
                print(f"Nenhum personagem encontrado com o id {personagem_id}")
                return None
        except Exception as error:
            print(f"Ocorreu um erro ao ler o personagem: {error}")
            return None

    def update_personagem(self, personagem_id: str, nome: str) -> bool:
        try:
            result = self.db.collection.update_one({"_id": ObjectId(personagem_id)}, {"$set": {"nome": nome}})
            if result.modified_count > 0:
                print(f"Personagem {personagem_id} atualizado com sucesso.")
                return True
            else:
                print(f"Nenhum personagem encontrado com o id {personagem_id}")
                return False
        except Exception as error:
            print(f"Ocorreu um erro ao atualizar o personagem: {error}")
            return False

    def delete_personagem(self, personagem_id: str) -> bool:
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(personagem_id)})
            if result.deleted_count > 0:
                print(f"Personagem {personagem_id} deletado com sucesso.")
                return True
            else:
                print(f"Nenhum personagem encontrado com o id {personagem_id}")
                return False
        except Exception as error:
            print(f"Ocorreu um erro ao deletar o personagem: {error}")
            return False