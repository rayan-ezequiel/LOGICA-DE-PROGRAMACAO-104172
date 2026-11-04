import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

lista_de_pacientes = []


while True:
    
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1. Cadastrar paciente')
    print('2. Listar pacientes')
    print('3. Atualizar paciente')
    print('4. Excluir paciente')
    print('0. Sair')
    
    opcao = int(input('Escolha: '))
    
    match opcao:
        # MENU CADASTRO
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            nome = input('Digite seu nome: ')
            sobrenome = input('Digite seu sobrenome: ')
            nome_e_sobrenome = nome + ' ' + sobrenome
            lista_de_pacientes.append(nome_e_sobrenome)
        # LISTAGEM
        case 2:
            print('LISTA DE PACIENTES\n')
            if len(lista_de_pacientes) == 0:
                print('Sem pacientes cadastrados.')
            else:
                for i, paciente in enumerate(lista_de_pacientes):
                    print(f'{i+1}. {paciente}')
                print(f'Total de pacientes: {len(lista_de_pacientes)}')
                input('\nPressione uma tecla para continuar...')
        # ATUALIZAÇÃO
        case 3:
            print('ATUALIZAR PACIENTES')
            atualizar = input('Qual paciente deseja atualizar ? ')
            if atualizar in lista_de_pacientes:
                novo = input('Novo paciente: ')
                posicao = lista_de_pacientes.index(atualizar)
                lista_de_pacientes[posicao] = novo
                print('Paciente alterado com sucesso!')
            
            else:
                print('Paciente não encontrado!')
        
        # REMOÇÃO
        case 4:
            print('\nExcluir paciente')
            nome = input('Qual paciente deseja remover? ')
            if nome in lista_de_pacientes:
                novo = input('Novo nome: ')
                posicao = lista_de_pacientes.remove(nome)
                print('Paciente excluído com sucesso!')
            else:
                print('Paciente não encontrado!')