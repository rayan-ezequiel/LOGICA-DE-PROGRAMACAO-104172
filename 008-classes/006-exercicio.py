from dataclasses import dataclass
import os

os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'Email: {self.email}')
        print('=' * 30)
    
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print('=' * 30)
    
    def whatsapp_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('=' * 30)

lista_de_cliente = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome= input('Digite seu nome: '),
        telefone= input('Digite seu telefone: '),
        email= input('Digite seu email: ')
    )
    lista_de_cliente.append(dados_do_cliente)

print('\nEXIBINDO DADOS\n')
for cliente in lista_de_cliente:
    cliente.mostrar_dados()
print('\nEXIBINDO E-MAIL MARKETING\n')
for cliente in lista_de_cliente:
    cliente.email_marketing()
print('\nEXIBINDO WHATSAPP MARKETING\n')
for cliente in lista_de_cliente:
    cliente.whatsapp_marketing()