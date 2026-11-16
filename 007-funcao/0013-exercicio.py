import os
os.system('cls' if os.name == 'nt' else 'clear')

def verificar_valor(valor):
    
    if valor <0:
        resultado = 'Negativo'
    elif valor == 0:
        resultado = 'Neutro'
    else:
        resultado = 'Positivo'
    
    return resultado
\
valor = int(input('Digite um número: '))

resultado = verificar_valor(valor)
print(f'O número {valor}\nÉ {resultado}')

