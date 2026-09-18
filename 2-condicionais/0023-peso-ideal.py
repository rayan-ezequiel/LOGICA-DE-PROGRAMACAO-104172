import os
os.system('cls')

print('Peso Ideal')

sexo = input('Qual seu sexo ? ').lower()
altura = float(input('Qual sua altura ? '))

match sexo:
    case 'masculino':
        print(f'Peso ideal: {((72.7 * altura) - 58):.2f}')
    case 'feminino':
        print(f'Peso ideal: {((62.1 * altura) - 44.7):.2f}')