salar = float(input('Qual o salário do funcionario? R$'))
plus = float(input('Qual foi o aumento? %'))
total = salar + (salar * plus / 100)
print('Um funcionario que ganhava R${:.2f}, com {:.0f} de aumento, passa a receber R${:.2f}'.format(salar, plus, total))
