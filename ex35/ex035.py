print('<==>'*12)
print('ANALISADOR DE TRIANGULOS')
print('<==>'*12)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulo.')
else:
    print('Os segmentos acima não podem formar triangulo.')

