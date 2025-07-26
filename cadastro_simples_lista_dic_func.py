listaProdutos = []

def menu():
    print()
    print("=" * 40)
    print("         BEM-VINDO AO SISTEMA")
    print("=" * 40)
    print("1 - Cadastrar Produto")
    print("2 - Vizualizar Produstos Cadastrados")
    print("3- Sair")
    entrada  = int(input("Digite a opção... : "))
    if entrada == 1:
            cadastrar_produto()
    elif entrada == 2:
            imprimir()
            if not listaProdutos:
                print("=" * 40)
                print("AINDA NÃO HÁ PRODUTOS CADASTRADOS")
                print("=" * 40)
                print()
    elif entrada ==3:
        exit()
    else:
            print("Opção Invalida")
            print()
            
def cadastrar_produto():
    nome = input("Digite o nome do Produto : ")
    preco = float(input("Digite o preço do Produto : "))
    quant = int(input("Digite a quantidade do Produto : "))
    newDictionary = {'nome':nome, 'preco':preco, 'quant':quant}
    listaProdutos.append(newDictionary)
    return listaProdutos

def imprimir():
    for newDictionary in listaProdutos:
        print()
        print(f"Produto : {newDictionary['nome']} ")
        print(f"Preço : {newDictionary['preco']:.2f} ")
        print(f"Quantidade : {newDictionary['quant']} ")


while True:
    menu()
