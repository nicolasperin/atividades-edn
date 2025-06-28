'''
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
'''

taxa_dolar = 5.2
taxa_euro = 6.15
valor_em_reais = 100
valor_convertido_para_euro = valor_em_reais * taxa_euro
valor_convertido_para_dolar = valor_em_reais * taxa_dolar

print(f"R${valor_em_reais:.2f} equivale a U${valor_convertido_para_dolar:.2f} ou €{valor_convertido_para_euro:.2f}")