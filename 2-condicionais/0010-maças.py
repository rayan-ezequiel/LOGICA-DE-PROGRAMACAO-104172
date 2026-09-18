import os
os.system('cls')


macas = int(input('Quantas maçã você vai querer: '))


if macas <= 12:
    print('a compra deu é: ', (macas * 1.30))
elif macas >= 12:
    print('a compra deu é: ', (macas * 1.00))
