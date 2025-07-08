def lerPalavra():
    palavra = str(input("Qual a palavra?: "))
    return palavra

def verificarPalindromo(palavra):
    if palavra == palavra[::-1]:
        print("Sim, a palavra é um palíndromo!")
    else:
        print("A palavra não é um palíndromo!")

def main():
    palavra = lerPalavra()
    verificarPalindromo(palavra)

main()