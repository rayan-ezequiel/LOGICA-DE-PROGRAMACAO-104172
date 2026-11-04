import os

lista_jogadores = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1. Cadastrar jogador')
    print('2. Listar jogadores')
    print('3. Atualizar jogador')
    print('4. Excluir jogador')
    print('0. Sair')
    
    opcao = int(input('\nEscolha: '))
    
    match opcao:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Cadastrar jogador\n')
            nome = input('Digite seu nome: ')
            sobrenome = input('Digite seu sobrenome: ')
            nome_e_sobrenome = nome + ' ' + sobrenome
            lista_jogadores.append(nome_e_sobrenome)
            print('\nJogador cadastrado com sucesso!')
            input('\nPressione Enter para voltar ao menu...')
        
        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Lista de jogadores\n')
            if len(lista_jogadores) == 0:
                print('Sem jogadores cadastrados.')
            else:
                for i, jogador in enumerate(lista_jogadores):
                    print(f'{i+1}. {jogador}')
                print(f'\nTotal de jogadores: {len(lista_jogadores)}')
            input('\nPressione Enter para voltar ao menu...')
        
        case 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Atualizar jogador\n')
            atualizar = input('Qual jogador deseja atualizar (digite o nome completo)? ')
            if atualizar in lista_jogadores:
                novo = input('Novo nome do jogador: ')
                posicao = lista_jogadores.index(atualizar)
                lista_jogadores[posicao] = novo
                print('\nJogador alterado com sucesso!')
            else:
                print('\nJogador não encontrado!')
            input('\nPressione Enter para voltar ao menu...')
        
        case 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Excluir jogador\n')
            nome = input('Qual jogador deseja remover (digite o nome completo)? ')
            if nome in lista_jogadores:
                lista_jogadores.remove(nome)
                print('\nJogador excluído com sucesso!')
            else:
                print('\nJogador não encontrado!')
            input('\nPressione Enter para voltar ao menu...')
            
        case 0:
            print('\nSaindo do programa...')
            break
            
        case _:
            print('\nOpção inválida! Tente novamente.')
            input('\nPressione Enter para voltar ao menu...')