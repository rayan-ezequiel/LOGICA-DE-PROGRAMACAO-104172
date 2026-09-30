import os
os.system('cls')

while True:
    nota = int(input('Digite sua nota: '))
    if nota >= 0 or nota >= 10:
        print(f'A sua nota é: {nota}')
    else:
        print('Coloque sua nota novamente.')
        break
print('Fim')
