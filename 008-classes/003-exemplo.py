from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Cliente:
    # Nome da variavel: tipo da variavel
    nome: str
    idade: int

lista_cliente = []
    
# SOLICITANDO DADOS DE UM CLIENTE
lista_cliente.append(Cliente('Marta',30))
lista_cliente.append(Cliente('José',40))

for cliente in lista_cliente:
    print(f'Nome: {cliente.nome}')
    print(f'idade: {cliente.idade}')
    print('='*15)
