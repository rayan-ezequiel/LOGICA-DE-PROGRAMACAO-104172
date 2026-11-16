import os

os.system('cls' if os.name == 'nt' else 'clear')

def media(notas):
    return sum(notas) / len(notas)

def aprovacao(resultado):
    if resultado >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

def notas_media(notas, resultado, situacao):
    print('\n--- Resultado ---')
    for i, nota in enumerate(notas, start=1):
        print(f'{i}ª nota: {nota:.1f}')
    print(f'Sua média é: {resultado:.2f}')
    print(f'Situação: {situacao}')

notas = []

for i in range(2):
    while True:
        nota = float(input(f'Digite sua {i + 1}ª nota: '))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print('Valor inválido! Digite uma nota entre 0 e 10.')

resultado = media(notas)
situacao = aprovacao(resultado)
notas_media(notas, resultado, situacao)