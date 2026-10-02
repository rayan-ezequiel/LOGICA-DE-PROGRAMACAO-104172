import os
os.system('cls')

soma = 0
vezes = 1
QUANTIDADE = 2
for i in range(QUANTIDADE):
    while True:
        nota = float(input(f'Digite sua {vezes}º nota: '))
        if nota < 0 or nota > 10:
            print('Nota invalida. Tente novamente...')
            input('Pressione qualquer tecla para continuar. ')
            os.system('cls')

        else:
            soma += nota
            break
        vezes += 1
media = soma / 2

print(f'Média: {media}')