import random
st = str(input('Primeiro nome: '))
nd = str(input('Segundo nome: '))
rd = str(input('Terceiro nome: '))
th = str(input('Quarto nome: '))
tudo = random.choice([st, nd, rd, th])
print('O nome escolhido foi {}'.format(tudo))
