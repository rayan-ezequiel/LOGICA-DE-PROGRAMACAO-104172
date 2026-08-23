# 1. Solicite a largura (float)
# 2. Solicite a altura (float)
# 3. Calcule a área
# 4. Exiba os dados digitados e a área final em metros quadrados
import os
os.system('cls')

print('= Calculo de area do quadrado =')

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = float(largura * altura)

print('a area é : ', area,'m2')