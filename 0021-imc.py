import os
os.system('cls')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite o seu altura: '))
imc =  peso / (altura * altura)

if imc < 18.6:
    print('Você está abaixo do peso')
elif imc >= 18.6 and imc <= 24.9:
    print('Você está no peso ideal')
elif imc >= 25 and imc <= 29.9:
    print('Você está levemente acima do peso')
elif imc >= 30.00 and imc <= 34.9:
    print('Você está no Obseidade grau 1')
elif imc >= 35.00 and imc <= 39.9:
    print('Você está no Obseidade grau 2')
elif imc >= 40:
    print('Você está no Obseidade grau 3')
