def validar_email(email: str) -> bool:
    if '@' in email:
        return True
    return False
    
def validar_nome(nome: str) -> bool:
    if len(nome) > 10:
        return True



    return False
    
