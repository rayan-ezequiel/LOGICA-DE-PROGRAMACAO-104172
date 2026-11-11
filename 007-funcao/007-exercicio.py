import os
os.system('cls')
nome = ""
telefone = ""
def cadastrar_cliente():
    global nome
    global telefone
    nome = input('Digite seu nome: ')
    telefone = int(input('Digite seu telefone: '))
def mostrar_dados():
    print(f'Nome do cliente: {nome}')
    print(f'Telefone do cliente: {telefone}')
    
while True:
    print('Código | Descrição')
    print('  1    | Adicionar pessoa')
    print('  2    | Exibir resultados')
    print('  0    | Sair')
    
    
    escolha = int(input('Escolha: '))
    
    match escolha:
        case 1:
            cadastrar_cliente()
        case 2:
            if nome or telefone == "":
                input('Você não colocou nenhum dado tente novamente.\nPressione qualquer tecla para continuar...')
                os.system('cls')
                continue
            else:
                mostrar_dados()
        case 0:
            break
        case _:
            print('Esse valor nao existe...')