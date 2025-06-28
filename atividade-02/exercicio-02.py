'''
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

'''
nome_do_produto = "Camiseta"
preco_original = 50
desconto = 0.2

valor_do_desconto = preco_original * desconto

preco_final = preco_original - valor_do_desconto

print(f"Nome do produto: {nome_do_produto}\nPreço original: {preco_original}\nPorcentagem de desconto: {desconto * 100}\nValor do desconto: {valor_do_desconto}\nPreço final: {preco_final}")