from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Cliente:
    # Nome da variavel: tipo da variavel
    nome: str
    idade: int
    altura: float
    peso: float

lista_cliente = []

# SOLICITANDO DADOS DE UM CLIENTE
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('\nDigite seu nome: '),
        idade= int(input('Digite sua idade: ')),
        altura = float(input('Digite sua altura: ')),
        peso = float(input('Digite seu peso: '))
    )
    lista_cliente.append(dados_do_cliente)
print('\nEXIBINDO DADOS\n')
for cliente in lista_cliente:
    print(f'Nome: {cliente.nome}.')
    print(f'Idade: {cliente.idade} anos.')
    print(f'Altura: {cliente.altura:.2f}.')
    print(f'Peso: {cliente.peso:.2f} kg')
    print('=' * 15)