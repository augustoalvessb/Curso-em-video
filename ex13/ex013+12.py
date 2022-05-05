preço = float(input('Preço do produto:R$'))
desc = float(input('Qual será o desconto? % '))
plus = float(input('Qual será o aumento? % '))
avist = preço - (preço * desc / 100)
prazo = preço + (preço * plus / 100)
print('De R${:.2f}, a vista com desconto sairá R${:.2f} e a prazo sairá R${:.2f}'.format(preço, avist, prazo))

