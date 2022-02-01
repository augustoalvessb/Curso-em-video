preco = float(input('Qual o preço do produto: R$'))
desc = float(input('Qual é o desconto: % '))
total = preco - (preco * desc / 100)

print('O produto que custava R${:.2f}, com o seu desconto de {:.0f}% irá custar R${:.2f}.'.format(preco, desc, total))

