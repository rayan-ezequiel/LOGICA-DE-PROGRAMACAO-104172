import os
import time

os.system('cls')

soma = 0
vezes = 1
QUANTIDADE = 3
for i in range(QUANTIDADE):
    while True:
        nota = float(input(f'Digite sua {vezes}º nota: '))
        vezes += 1
        if nota < 0 or nota > 10:
            print('Nota invalida. Tente novamente...')
            input('Pressione qualquer tecla para continuar. ')
            os.system('cls')
        else:
            soma += nota
            break
        
media = soma / 3

if media >= 7:
    print('Aprovado.')
elif 5 < media < 6.9:
    print('Em recuperação.')
elif media <= 5:
    print('Reprovado.')
print(f'Média: {media}')