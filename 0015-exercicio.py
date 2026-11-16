import os

os.system('cls' if os.name == 'nt' else 'clear')

def metro_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

metros = float(input('Digite a quantidade de metros: '))
centimetros = metro_para_centimetros(metros)

print(f'{metros} metro(s) equivalem a {centimetros} centímetros.')