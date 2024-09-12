from models.abstract.fisica import Fisica #Import Abstracts 
from models.endereco import Endereco #Import Classes
from models.enums.sexo import Sexo #Import Enums

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, protocolo:int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)

        self.protocolo = protocolo

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProtocolo de Atendimento: {self.protocolo}"
        )