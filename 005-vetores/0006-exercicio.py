import os
os.system('cls')

notas = []
vez = 1

while True:
    
    nota = float(input(f'Digite sua {vez}º nota: '))
    notas.append(nota)
    vez += 1
    
    if len(notas) == 4:
        media = sum(notas) / len(notas)
        
        if media >= 7:
            print(f'O aluno está aprovado com média: {media}')
            
        elif media >= 5:
            print(f'O aluno está em recuperação com média: {media}')

        elif media < 5:
            print(f'O aluno está reprovado com média: {media}')
        
        print(f'1º Nota: {notas[0]}')
        print(f'2º Nota: {notas[1]}')
        print(f'3º Nota: {notas[2]}')
        print(f'4º Nota: {notas[3]}')
        
        break