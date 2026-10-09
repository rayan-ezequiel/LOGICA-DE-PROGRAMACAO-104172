import os
os.system('cls')

n1 = float(input('Digte numero: '))
n2 = float(input('Digte numero: '))
n3 = float(input('Digte numero: '))

media = (n1 + n2 + n3 / 3)
if media >= 7:
    print('voce foi aprovado')
elif media < 7:
    print('voce foi reprovado')