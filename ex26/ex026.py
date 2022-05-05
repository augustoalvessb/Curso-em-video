frase = str(input('Digite uma Frase: ')).strip().upper()
con = frase.count('A')
pri = frase.find('A')+1
ult = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase.'.format(con))
print('A primeira letra A apareceu na posição {}'.format(pri))
print('A ultima letra A apareceu na posição {}'.format(ult))

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A pareceu na posição {}'.format(frase.rfind('A')+1))
