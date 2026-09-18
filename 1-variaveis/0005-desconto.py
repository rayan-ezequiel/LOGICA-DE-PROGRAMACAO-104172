import os 

os.system('cls')


print("= valor com desconto =")
valor = int(input('Digite o valor: '))


desconto = (valor * 0.10)
valor_com_desconto = valor - desconto

print('O valor é: ', valor)
print('O desconto é: 10%')
print("O valor com o desconto é:", valor_com_desconto)
