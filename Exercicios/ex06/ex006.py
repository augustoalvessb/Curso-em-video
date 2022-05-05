n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {} \nO triplo de {} é {} \nE a raiz quadrada de {} é {:.2f}'.format(n, d, n, t, n, r))
print('O dobro desse numero é {} \nO triplo desse numero é {} \nE a raiz quadrada desse número é {:.2f}'.format((n*2), (n*3), (n**(1/2))))
print('A raiz quadrada de {} é {}'.format(n, pow(n, (1/2))))
print('O dobro desse numero é {}, O triplo desse numero é {}, E a raiz quadrada desse número é {:.2f}'.format((n*2), (n*3), pow(n, (1/2))))

