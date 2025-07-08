def lerOpcao():
    opcao = int(input("Informe a operação a ser realizada:\n\n1- Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n\n"))
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        opcao = input("Opção inválida!\n\nInforme a operação a ser realizada:\n\n1- Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n\n")
    return opcao

def lerNumero():
    try:
        num = float(input("Digite um número: "))
    except ValueError:
        num = float(input("O valor deve ser um número!\nDigite um número: "))
    return num
    
def calcular(x, y):
    op = lerOpcao()
    if op == 1:
        return x + y
    elif op == 2:
        return x - y
    elif op == 3:
        return x * y
    else:
        return x / y


def main():
    numero1 = lerNumero()
    numero2 = lerNumero()
    resultado = calcular(numero1, numero2)
    print(f"\nResultado: {resultado}")

main()