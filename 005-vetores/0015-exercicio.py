import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

lista_de_produtos = []

while True:
    
    os.system('cls')
    print('===MERCADINHO VALÉRIA')
    print('1 - Cadastrar produtos')
    print('2 - Listar produtos')
    print('3 - Atualizar produtos')
    print('4 - Remover produtos')
    print('5 - Buscar produtos')
    
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
            print('\nLISTA DE PRODUTOS\n')
            if len(lista_de_produtos) == 0:
                print('Estoque vazio.')
            else:
                for i, produto in enumerate(lista_de_produtos):
                    print(f'{i+1}. {produto}')
                print(f'Total de produtos: {len(lista_de_produtos)}')
                input('\nPressione uma tecla para continuar...')
        case 3:
            print('\nATUALZIAR PRODUTO')
            nome = input('Qual produto deseja atualizar? ')
            if nome in lista_de_produtos:
                novo = input('Novo nome: ')
                posicao = lista_de_produtos.index(nome)
                lista_de_produtos[posicao] = novo
                print('Produto alterado com sucesso!')
            else:
                print('Produto não encontrado.')
        case 4:
            print('\nREMOVER PRODUTO')
            nome = input('Qual produto deseja remover? ')
            if nome in lista_de_produtos:
                novo = input('Novo nome: ')
                posicao = lista_de_produtos.remove(nome)
                print('Produto excluído com sucesso!')
            else:
                print('Produto não encontrado.')
        case 5:
            print('\nENCONTRAR PRODUTO')
            nome = input('Qual produto deseja buscar? ')
            if nome in lista_de_produtos:
                print('Produto encontrado com sucesso!')
            else:
                print('Produto não está no estoque...')
    
        case 0:
            print('Finalizando programa...')
            time.sleep(3)
            break
            
        case _:
            print('Opção inválida!')
            input('Pressione uma tecla para continuar...')

