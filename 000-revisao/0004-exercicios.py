import os
import time
os.system('cls')

s = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    s += i
print("Sum é:", s)