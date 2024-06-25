nome = 'Mario Henrique'
altura = 1.73
peso = 90
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

print(linha_1)
print(linha_2)
print(linha_3)

# Mario Henrique tem 1.73 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

''' aprendendo a base de string / uma introdução ao f-string'''