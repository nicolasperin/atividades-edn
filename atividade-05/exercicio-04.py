from datetime import datetime

def calcular_dias_vivo():
    dataNascStr = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    try:
        dataNasc = datetime.strptime(dataNascStr, "%d/%m/%Y")
        dataAtual = datetime.now()
        diferenca = dataAtual - dataNasc
        return diferenca.days
    except ValueError:
        print("Data inválida! Use o formato dd/mm/aaaa.")

def main():
    diasVivo = calcular_dias_vivo()
    print(f"Você está vivo há {diasVivo} dias!")

main()