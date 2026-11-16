import os
os.system('cls' if os.name == 'nt' else 'clear')

notas = []

def media(notas):
    resultado = sum(notas) / len(notas)
    return resultado

for i in range(3):
    nota = float(input(f'Digite sua {i + 1}º nota: '))
    notas.append(nota)

resultado = media(notas)
print(f'Sua média é: {resultado}')