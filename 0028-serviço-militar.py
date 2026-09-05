import os
os.system('cls')

print('Serviço militar')

sexo_de_registro = input('Qual seu sexo ? ').lower()
ano_de_nascimento = int(input('Qual sua data de nascimento ? '))


if sexo_de_registro == 'masculino':
    ano_de_nascimento = (2026 - ano_de_nascimento)
    print(f'Você deve se apresentar ao serviço militar obrigatório {ano_de_nascimento}')
else: print('Não deve se apresentar.')