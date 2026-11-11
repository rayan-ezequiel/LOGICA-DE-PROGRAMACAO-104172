import os

os.system('cls')

@dataclass
class Produto:
    nome: str
    preco: float
lista_produtos = []
def solicitar_dados():
    for i in range(3):
        produto = Produto(
            nome = input('Digite o nome do produto: ')
            preco = int(input('Digite o preço do produto: '))
            
        )
        lista_produtos.append(produto)

def mostrar_dados(lista_produtos):
    for produto in lista_produtos:
        print(f'{produto.nome} custa R$ {produto.preco}')
        
print('= SOLICITANDO DADOS =')

solicitar_dados()

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)