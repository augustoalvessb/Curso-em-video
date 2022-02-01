larg = float(input('Largura de parede: '))
altu = float(input('Altura da parede: '))
a = larg * altu
t = a / 2
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m².'.format(larg, altu, a))
print('Para pinta essa parede, você precisará de {:.2f}l de tinta.'.format(t))