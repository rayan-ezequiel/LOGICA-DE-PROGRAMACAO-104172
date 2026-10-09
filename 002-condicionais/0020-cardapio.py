import os
os.system('cls')

print('Cardápio Restaurante')

print('\n Código   |     Prato               |       Valor ')
print('\n 1	  | Picanha	            | R$ 25,00 ')
print('\n 2	  | Lasanha	            | R$ 20,00 ')
print('\n 3	  | Strogonoff	            | R$ 18,00 ')
print('\n 4	  | Bife Acebolado	    | R$ 15,00 ')
print('\n 5	  | Pão com ovo	            | R$ 5,00 ')

escolha = int(input('\nDigite o Código do prato que deseja: '))

match escolha:
    case 1:
        print('Você escolheu Picanha, o valor do prato é: R$ 25,00')
    case 2:
        print('Você escolheu Lasanha, o valor do prato é: R$ 20,00')
    case 3:
        print('Você escolheu Strogonoff, o valor do prato é: R$ 18,00')
    case 4:
        print('Você escolheu Bife Acebolado, o valor do prato é: R$ 15,00')
    case 5:
        print('Você escolheu Pão com ovo, o valor do prato é: R$ 5,00')
