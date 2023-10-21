from cadastro import (
    cadastrar_usuario,
    obter_usuario,
    alterar_senha
)

from getpass import getpass

while True:
    print('Olá, Bem-vindo aos sistema de cadastro')
    print('1 - Cadastrar o usuário')
    print('2 - Exibir o usuário')
    print('3 - Sair do programa')
    
    escolha = int(input('Digite a sua escolha: '))
    
    if escolha == 1:
        nome = input('Digite o nome do usuário: ')
        idade = int(input('Digite a idade do usuário: '))
        email = input('Digite o email do usuário: ')
        endereco = input('Digite o endereço do usuário: ')
        print('''Digite sua senha contendo os seguintes caracteres:
                 Ao menos 10 caracteres
                 Contendo caractere especial
                 Contendo Número
              ''')
        senha = getpass('Digite sua senha: ')
        print(cadastrar_usuario(nome, idade, email, endereco, senha))
    elif escolha == 2:
        email = input('Digite o email do usuário: ')
        print(obter_usuario(email))
        
        print('Deseja alterar sua senha?')
        print('1 - Sim')
        print('2 - Não')
        escolha2 = int(input('Escolha: '))
        
        if escolha2 == 1:
            nova_senha = getpass('Digite sua nova senha: ')
            senha_alterada = alterar_senha(email, nova_senha)
            print(senha_alterada)
            continue
        continue
        
    elif escolha == 3:
        print('Tchau parceiro')
        break
    else:
        print('Opção inválida')
        continue    