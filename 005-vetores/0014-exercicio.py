import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

lista_de_series = []

while True:

    print('SÉRIES DENDEZEIROS')
    print('1 - GUARDAR SÉRIE')
    print('2 - LISTAR SÉRIES')
    print('0 - SAIR')

    opcao = input('Escolha: ')
    match opcao:
        case 1:
            print('\nCADASTRO DE SÉRIE')
            nome = input('Digite o nome da série: ').strip().lower()
            if nome == '':
                print('Digite algo.')
                time.sleep(2)
            
            elif nome in lista_de_series:
                print('Essa série já existe...')
                time.sleep(2)
            
            else:
                lista_de_series.append(nome)
                print('Série Cadastrado Com sucesso!')
                time.sleep(2)
            
        case 2:
            print('CATALÓGO DE SÉRIES\n')
            if len(lista_de_series) == 0:
                print('Estoque vazio.')
            else:
                for i, produto in enumerate(lista_de_series):
                    print(f'{i+1}. {produto}')
                print(f'Total de séries: {len(lista_de_series)}')
                input('\nPressione uma tecla para continuar...')
            
        case 0:
            print('Finalizando programa...')
            time.sleep(3)
            break
            
        case _:
            print('Opção inválida!')
            input('Pressione uma tecla para continuar...')