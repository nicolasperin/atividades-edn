def lerConta():
    valor = float(input("Qual o valor da conta: "))
    while valor < 0:
        valor = float(input("Valor inválido!\nDigite o valor da conta: "))
    return valor

def lerPorc():
    porc = int(input("Qual a porcentagem da gorgeta: "))
    while porc < 0: 
        porc = int(input("Valor inválido!\nQual a porcentagem da gorgeta: "))
    return porc

def calcGorgeta(valorConta, desconto):
    return valorConta*(desconto/100)

def main():
    valor = lerConta()
    desc = lerPorc()
    gorgeta = calcGorgeta(valor, desc)
    print(f"O valor da conta foi R${valor:.2f}, e a gorgeta de {desc}% ficou R${gorgeta:.2f}")

main()