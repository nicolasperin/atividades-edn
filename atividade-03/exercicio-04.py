'''
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
'''
ano = int(input("Informe o ano: "))

if (ano % 4 == 0 and not ano % 400 != 0 ):
    print("Ano bissexto")
else:
    print("Não é ano bissexto")