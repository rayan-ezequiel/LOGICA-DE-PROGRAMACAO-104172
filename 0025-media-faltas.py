import os 
os.system('cls')

print('Média')

media = float(input('Qual foi sua média ? '))
numero_de_faltas = float(input('Quantas vezes você faltou ? '))

if media >= 7.0 and numero_de_faltas <=40:
    print('Você foi aprovado')
else: print('Você foi reprovado')