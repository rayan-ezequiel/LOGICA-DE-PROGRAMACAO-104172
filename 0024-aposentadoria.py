import os 
os.system('cls')

print('Aptidão Para Aposentadoria')

matricula = input('Qual sua matricula ? ')
ano_de_nascimento = float(input('Qual seu ano de nascimento ? '))
tempo_de_trabalho = float(input('Qual seu tempo de trabalho ? '))
idade = (2026 - ano_de_nascimento)

print(f'O seu codigo é: {matricula}\n')
print(f'Sua idade é: {idade}\n')
print(f'Seu tempo de trabalho é: {tempo_de_trabalho}\n')

if idade >= 65 or tempo_de_trabalho >= 30:
    print('Requerer aposentadoria')
else: print('Não requer aposentadoria')



