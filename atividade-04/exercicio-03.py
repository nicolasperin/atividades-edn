def lerSenha():
    senha = input("Informe a sua senha: ")
    while len(senha) < 8 or not any(i.isdigit() for i in senha):
        senha = input("A senha deve er maior que 8 caracteres e deve conter pelo menos um número!\nDigite a senha: ")
    return senha

def main():
    senha = lerSenha()
    print(f"Sua senha segura é {senha}")

main()