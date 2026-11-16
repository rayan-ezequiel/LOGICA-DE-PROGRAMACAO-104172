import os
import time
os.system('cls' if os.name == 'nt' else 'clear')



ano_atual = time.localtime().tm_year
def idade(ano_de_nascimento):
    resultado = ano_atual - ano_de_nascimento
    return resultado

ano_de_nascimento = int(input('Digite o ano de nascimento: '))
resultado = idade(ano_de_nascimento)

print(f'Ano atual: {ano_atual}.\nSua idade: {resultado}.')