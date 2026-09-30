import os
os.system('cls')

nota = 0
vezes = 1

QUANTIDADE = 0

print('MÉDIA')
for i in range(4):
    nota += int(input(f'Digite sua {vezes}º nota: '))
    vezes += 1
    media = nota / 4
print(f'Sua média: {media}')

