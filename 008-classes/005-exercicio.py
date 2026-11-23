from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass

class Cliente:
    nome: str
    telefone: str
    email: str

lista_de_cliente = []

dados_do_cliente = Cliente(
    nome = input('Digite seu nome: '),
    telefone = input('Digite seu telefone: '),
    email = input('Digite seu email: ')
)
lista_de_cliente.append(dados_do_cliente)

print('\nEXIBINDO DADOS\n')
for cliente in lista_de_cliente:
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'Email: {cliente.email}')
    print('='*15)