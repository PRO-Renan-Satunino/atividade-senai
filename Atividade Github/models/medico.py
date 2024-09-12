from models.abstract.funcionario import Funcionario #Import Abstracts
from models.endereco import Endereco #Import Classes
#Import Enums
from models.enums.setor import Setor
from models.enums.sexo import Sexo

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)

        self.crm = crm

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCRM: {self.crm}"               
        )