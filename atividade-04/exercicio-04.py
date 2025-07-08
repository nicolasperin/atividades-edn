def lerNumero():
    while True:
        try:
            num = int(input("Digite um número: "))
            break
        except ValueError:
            num = int(input("Digite um número: "))
            break
    return num

def lerVetorNumeros(vetorNumeros):
    for i in range(5): # Lê 5 números
        num = lerNumero()
        vetorNumeros.append(num)

def separaNumeros(vetorNumeros, vetorPar, vetorImpar):
    for numero in vetorNumeros:
        if numero % 2 == 0:
            vetorPar.append(numero)
        else:
            vetorImpar.append(numero)

def main():
    vetorNumeros = []
    vetorPar = []
    vetorImpar = []
    lerVetorNumeros(vetorNumeros)
    separaNumeros(vetorNumeros, vetorPar, vetorImpar)
    print(f"Dos números informados, {len(vetorPar)} são números pares e {len(vetorImpar)} são números ímpares")
    print(f"Números pares: {vetorPar}")
    print(f"Números ímpares: {vetorImpar}")

main()