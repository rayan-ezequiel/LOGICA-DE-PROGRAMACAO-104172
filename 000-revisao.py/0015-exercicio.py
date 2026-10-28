import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

numeros = []

print('Buscador e Contador em Vetor')
for i in range(10):
    try:
        
        numero = int(input(f'Digite o {i + 1}º numero: '))
        numeros.append(numero)
    
    except ValueError:
        print('ERROR: Digite um número inteiro.')
        break

    if len(numeros) == 10:
        while True:
            try:
                numero_para_busca = int(input('Digite um número para buscar: '))

            except ValueError:
                print('ERROR: Digite um número inteiro.')
                continue
            
            if numero_para_busca in numeros:
                quantidade = numeros.count(numero_para_busca)
                print(f'O número: {numero_para_busca} aparece {quantidade} vezes na lista.')

                while True: 
                    try:
                        saida = int(input('[1]- Para realizar uma nova busca.\n[2]- Para sair.\nEscolha: '))
                    except ValueError:
                        print('Digite um número inteiro')
                        continue
                    if saida == 1:
                        break
                    elif saida == 2:
                        sys.exit()
                    else:
                        print('Opcção inválida. tente novamente.')
                        continue
            
            elif numero_para_busca not in numeros:
                print(f'O número: {numero_para_busca} não está presente na lista, Tente outro.')
                continue
            
    
