import os
os.system('cls' if os.name == 'nt' else 'clear')

notas = []

def media(notas):
    resultado = sum(notas) / len(notas)
    return resultado

for i in range(3):
    nota = float(input(f'Digite sua {i + 1}º nota: '))
    notas.append(nota)

def notas_media(notas, resultado):
    for i, nota in enumerate(notas, start=1):
        print(f'{i}ª nota: {nota}')
    print(f'Sua média é: {resultado:.2f}')

resultado = media(notas)
print(f'Sua média é: {resultado}')
notas_media(notas, resultado)