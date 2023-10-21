from validacoes import (
    validar_email, 
    validar_nome,
   
)

usuarios = {}

def cadastrar_usuario(
    nome: str, 
    idade: int, 
    email: str, 
    endereco: str,
    senha: str) -> dict:
    
    if validar_nome(nome) and validar_email(email):        
        usuario = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "endereco": endereco,
            "senha": senha
        }
        
        usuarios[email] = usuario
        
        print('Valores inseridos com sucesso')
        
        return usuarios
    return 'Algum dos valores está errado!'


def obter_usuario(email: str):
    if email in usuarios:
        return usuarios[email]
    return f'Esse email: {email} não existe'   


def alterar_senha(email: str, senha: str):
    if email in usuarios:
        usuarios[email]['senha'] = senha
        return 'A senha foi alterada com sucesso!'
    return 'Usuário não encontrado'