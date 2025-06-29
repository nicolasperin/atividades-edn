'''
Data de entrega: 30 de jun., 13:00
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
'''

idade = int(input("Informe a idade: "))

if idade >= 60:
    categoria = "Idoso"
elif idade >= 18:
    categoria = "Adulto"
elif idade >= 13:
    categoria = "Adolescente"
elif idade >= 0:
    categoria = "Criança"
else:
    categoria = "Idade inválida"

print(categoria)