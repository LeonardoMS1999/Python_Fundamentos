alunos = []

def cadastrar_aluno():  
    nome = str(input("Dgite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    dic = {'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': media}
    alunos.append(dic)

def exibir_alunos():
    for aluno in alunos:
        print()
        print(aluno)

def menu():

    while True:
        print('=' * 40)
        print('Bem vindo !')
        print('=' * 40)
        print()
        print('1 – Cadastrar aluno')
        print('2 – Exibir todos os alunos')
        print('3 – Sair')
        print()
        entrada = int(input("Digite uma opção : >>> "))
        if entrada == 1:
            cadastrar_aluno()
        elif entrada == 2:
            exibir_alunos()
        elif entrada == 3:
            break
        else:
            print()
            print('ENTADA INVALIDA')


menu()