import os
os.system('cls')

nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / (2)


if media >= 9:
    print('você foi aprovado no conceito A')
elif media >= 7.5 and media < 9:
    print('você foi aprovado no conceito B')
elif media >= 6 and media < 7.5:
    print('você foi aprovado no conceito C')
elif media >= 4 and media < 6:
    print('você foi aprovado no conceito D')
elif media < 4:
    print('você foi aprovado no conceito ')















