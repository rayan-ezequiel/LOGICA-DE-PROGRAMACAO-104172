import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Controle de Temperatura Semanal')

# Controle de Temperatura Semanal VETORESMAX/MIN FOR
# Guarde a temperatura média dos 7 dias da semana em um vetor. Identifique a maior e a menor temperatura do
# período e exiba o nome/número de cada dia (ex: Dia 1, Dia 4) em que a temperatura superou os 30°C.

temperatura30 = []
temperaturas = []
dias = []

for i in range(7):
    dia = i + 1
    temperatura = float(input(f'Digite a {i + 1}º temperatura: '))
    
    if temperatura > 30:
        dias.append(dia)
        temperatura30.append(temperatura)
        
    else:
        temperaturas.append(temperatura)

print(f'Maior Temperatura: {max(temperaturas)}°C\nMenor Temperatura: {min(temperaturas)}°C')
print(f'Nos dias: {dias}, a temperatura superou 30°C.')



