from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Paciente:
    nome: str
    idade: str
    telefone: str
    endereco: str
    
    def todos_dados(self):
        print(f'Nome do paciente: {self.nome}')
        print(f'Idade do paciente: {self.idade}')
        print(f'Telefone do paciente: {self.telefone}')
        print(f'Endereço do paciente: {self.endereco}')
        print('=' * 30)

    def nome_idade_paciente(self):
        print(f'Nome do paciente: {self.nome}')
        print(f'Idade do paciente: {self.idade}')
        print('=' * 30)

    def nome_telefone_paciente(self):
        print(f'Nome do paciente: {self.nome}')
        print(f'Telefone do paciente: {self.telefone}')
        print('=' * 30)

        
lista_de_cliente = []
    
print('\nSOLICITANDO DADOS')
for i in range(2):
    dados_cliente = Paciente(
        nome = input('Nome do Paciente: '),
        idade = input('Idade do Paciente: '),
        telefone = input('Telefone do Paciente: '),
        endereco = input('Endereço do Paciente: ')
        )
            
    lista_de_cliente.append(dados_cliente)
        
print('\nEXIBINDO DADOS')
for pacientes in lista_de_cliente:
    print('=' * 30)
    print('TODOS OS DADOS')
    pacientes.todos_dados()
for pacientes in lista_de_cliente:
    print('=' * 30)
    print('NOME E IDADE DOS PACIENTES')
    pacientes.nome_idade_paciente()
for pacientes in lista_de_cliente:
    print('=' * 30)
    print('NOME E TELEFONE DOS PACIENTES')
    pacientes.nome_telefone_paciente()