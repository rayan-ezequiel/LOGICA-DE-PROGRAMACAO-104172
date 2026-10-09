import os
os.system('cls')

vezes = 1
nota = 0
QUANTIDADE = 3

print('MÉDIA')

for i in range(QUANTIDADE):
    nota += float(input(f"Digite sua {vezes}º nota: "))
    vezes += 1
    media = nota / 3
if media >= 7:
    print(f'O aluno está aprovado com média: {media:.2f}')
elif media <=4:
    print(f'O aluno está reprovado com média: {media:.2f}')
else: print(f'O aluno está em recuperação com média: {media:.2f}')