import os
import time
os.system('cls')



while True:
    nota_um = int(input('Digite sua primeira nota: '))
    nota_dois = int(input('Digite sua segunda nota: '))
    if nota_um < 0 or nota_um > 10 or nota_dois < 0 or nota_dois > 10:
        print('nota invalida digite novamente...')
        break
    media = (nota_um + nota_dois) / 2
    if media > 8:
        print('Parabéns você é barril.')
    else: print('talvez da próxima vez, você consiga ser competente.')
    print(f'Sua media é: {media}')
    break