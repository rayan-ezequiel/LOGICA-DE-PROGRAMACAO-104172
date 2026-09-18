import os
os.system('cls')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))


delta = float((b ** 2 -4 * a * c ))
print('O delta é: ',delta)

x1 = (-b + (delta ** 0.5)) / (2*a)
x2 = (-b - (delta ** 0.5)) / (2*a)

print('O valor de A= ', x1, 'O valor de B= ', x2)


































