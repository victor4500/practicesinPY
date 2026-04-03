#validador de senhas
import os

print('uma senha valida seria uma senha que tem no minimo 8 caracteres e uma letra maiuscula e um caractere espcial.')

senha = (input('Vamos ver se a sua senha é valida: '))

def validar_Ncaract(senha):
    return len(senha) >= 8
    
def validar_nume(senha):
    for letra in senha:
        if letra.isdigit():
            return True

    return False

especiais = "!@#$%&."

def validar_caract(senha):
    for especial in senha:
        if especial in especiais:
            return True
    
    return False
            
#resltado = validar_Ncaract(senha) and validar_nume(senha) and validar_caract(senha)

erros = []

if not validar_Ncaract(senha):
    erros.append("A senha deve conter no minimo 8 caracteres, poxa... foi aviado a cima")
    
if not validar_nume(senha):
    erros.append("já sabe onde errou né? a senha ta sem numero :(")

if not validar_caract(senha):
    erros.append("poxa errando de novo? sabe que precisade um caractere especial.")

if not erros:
    print("senha validaaa!, vc conseguiu <3")
else:
    print("senha n ta valida fi, faz uma senha decente ai pfvr")
    for erro in erros:
        print("***", erro)


def limpar_terminal():
    os.system("clear")

input("\nPara limpar o terminal precssione ENTRER...")
limpar_terminal() 


#if resltado:
 #   print('a senha valida')
#else:
 #   print('senha não valida')