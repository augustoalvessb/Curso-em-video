r = float(input('Quanto de dinheiro vôce tem na carteira? R$'))
d = r / 5.55
e = r / 6.70
y = r / 0.052
print('Com R${:.2f} você pode comprar U${:.2f}, '.format(r, d), end='')
print('U€{:.2f}, '.format(e), end='')
print('e U¥{:.2f}.'.format(y))