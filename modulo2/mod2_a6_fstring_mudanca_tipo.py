# Módulo 2 - Fstrings e Mudança de tipo de variáveis

faturamento = 2000
custo = 500
lucro = faturamento - custo

# print('O faturamento da loja foi {0}. O custo foi {1}. E o lucro foi de {2}.'.format(faturamento, custo, lucro))

# print('O faturamento da loja foi {}. O custo foi {}. E o lucro foi de {}.'.format(faturamento, custo, lucro))

print(f'O faturamento da loja foi {faturamento}. O custo foi {custo}. E o lucro foi de {lucro}.')

# Mudança de tipo de variáveis

faturamento_2 = int(input('Insira o faturamento da loja: '))
custo_2 = int(input('Insira o custo da loja: '))
lucro_2 = faturamento_2 - custo_2

print(lucro_2)