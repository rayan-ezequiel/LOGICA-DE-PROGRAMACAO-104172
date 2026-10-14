import os
os.system('cls')

notas = []
vez = 1

while True:
    
    nota = float(input(f'Digite sua {vez}º nota: '))
    notas.append(nota)
    vez += 1
    menor_nota = min(notas)
    maior_nota = max(notas)
    
    if len(notas) == 4:
        os.system('cls')
        media = sum(notas) / len(notas)
        for posicao, notas in enumerate(notas, start=1):
            print(f'{posicao}º: {notas}')
        print(f'Média: {media}')
        if media >= 7:
            print(f'O aluno está aprovado com média: {media}')
        elif media >= 5:
            print(f'O aluno está em recuperação com média: {media}')
        elif media < 5:
            print(f'O aluno está reprovado com média: {media}')
        print(f'Sua maior nota foi: {maior_nota}')
        print(f'Sua menor nota foi: {menor_nota}')

        break