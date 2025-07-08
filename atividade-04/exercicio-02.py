def lerNota():
    nota = float(input("Informe a nota: "))
    while nota < 0:
        nota = float(input("Nota inválida!\nInforme a nota: "))
    return nota

def calcMedia(vetorNotas):
    soma = 0
    for i in range(len(vetorNotas)):
        soma = soma + vetorNotas[i]
    media = soma / len(vetorNotas)
    return media

def lerVetorNotas(vetorNotas):
    for i in range(5): # Lê a nota de 5 alunos
        nota = lerNota()
        vetorNotas.append(nota) 

def main():
    vetorNotas = []
    lerVetorNotas(vetorNotas)
    media = calcMedia(vetorNotas)
    print(f"A média da sala é {media}")    

main()