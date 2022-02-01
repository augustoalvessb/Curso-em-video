a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O maior número é {}'.format(maior))
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {}'.format(menor))