import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

lista_de_produtos = []

while True:
    
    os.system('cls')
    print('===MERCADINHO DENDEZEIROS')
    print('1 - Cadastrar produtos')
    print('2 - Listar produtos')
    print('0 - Sair')

    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('\nCADASTRO DE PRODUTO')
            nome = input('Digite o nome do produto: ').strip().lower()
            if nome == '':
                print('Digite algo.')
                time.sleep(2)
            
            elif nome in lista_de_produtos:
                print('Esse produto já existe...')
                time.sleep(2)
            
            else:
                lista_de_produtos.append(nome)
                print('Produto Cadastrado Com sucesso!')
                time.sleep(2)
            
        case 2:
            print('LISTA DE PRODUTOS\n')
            if len(lista_de_produtos) == 0:
                print('Estoque vazio.')
            else:
                for i, produto in enumerate(lista_de_produtos):
                    print(f'{i+1}. {produto}')
                print(f'Total de produtos: {len(lista_de_produtos)}')
                input('\nPressione uma tecla para continuar...')
            
        case 0:
            print('Finalizando programa...')
            time.sleep(3)
            break
            
        case _:
            print('Opção inválida!')
            input('Pressione uma tecla para continuar...')

