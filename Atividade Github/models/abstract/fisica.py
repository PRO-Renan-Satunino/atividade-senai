from abc import ABC, abstractclassmethod
from models.endereco import Endereco #Import Classes
from models.enums.sexo import Sexo #Import Enum
from models.abstract.pessoa import Pessoa #Import Abstracts

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf:str, rg:str, dataNascimento:str, sexo:Sexo) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nSexo: {self.sexo.value}"
        )