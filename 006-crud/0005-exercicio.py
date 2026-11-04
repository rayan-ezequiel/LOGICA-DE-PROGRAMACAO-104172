import os
os.system('cls' if os.name == 'nt' else 'clear')

print('1. Cadastrar jogador')
print('2. Listar jogadores')
print('3. Atualizar jogador')
print('4. Excluir jogador')
print('0. Sair')

lista_jogadores = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1. Cadastrar jogadores')
    print('2. Listar jogadores')
    print('3. Atualizar jogadores')
    print('4. Excluir jogadores')
    print('0. Sair')
    
    opcao = int(input('Escolha: '))
    
    match opcao:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            nome = input('Digite seu nome: ')
            sobrenome = input('Digite seu sobrenome: ')
            nome_e_sobrenome = nome + ' ' + sobrenome
            lista_jogadores.append(nome_e_sobrenome)
        
        case 2:
            print('Lista de jogadores\n')
            if len(lista_jogadores) == 0:
                print('Sem jogadores cadastrados.')
            else:
                for i, jogadores in enumerate(lista_jogadores):
                    print(f'{i+1}. {jogadores}')
                print(f'Total de jogadores: {len(lista_jogadores)}')
                input('\nPressione uma tecla para continuar...')
        
        case 3:
            print('Atualizar jogadores')
            atualizar = input('Qual jogadores deseja atualizar ? ')
            if atualizar in lista_jogadores:
                novo = input('Novo jogadores: ')
                posicao = lista_jogadores.index(atualizar)
                lista_jogadores[posicao] = novo
                print('jogadores alterado com sucesso!')
            
            else:
                print('jogadores não encontrado!')
        
        
        case 4:
            print('\nExcluir jogadores')
            nome = input('Qual jogadores deseja remover? ')
            if nome in lista_jogadores:
                novo = input('Novo jogador: ')
                posicao = lista_jogadores.remove(nome)
                print('jogadores excluído com sucesso!')
            else:
                print('jogadores não encontrado!')