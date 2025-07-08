def lerValor():
    valor = float(input("Qual o valor da conta: "))
    while valor < 0:
        valor = float(input("Valor inválido!\nDigite o valor da conta: "))
    return valor

def lerPorc():
    porc = int(input("Qual a porcentagem de desconto?: "))
    while porc < 0: 
        porc = int(input("Valor inválido!\nQual a porcentagem de desconto?: "))
    return porc

def calcValorFinal(valor, desc):
    return valor - (valor*(desc/100))

def main():
    valor = lerValor()
    desc = lerPorc()
    valorFinal = calcValorFinal(valor, desc)
    print(f"Valor original do produto: R${valor:.2f}\nDesconto: {desc}%\nValor final após o desconto: R${valorFinal:.2f} ")

main()