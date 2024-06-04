velo = float(input('Qual a velocidade do carro? '))
multa = (velo - 80) * 7
if velo > 80:
    print('MULTADO! Você excedeu o limite de 80km/h.')
    print('A multa a ser paga será de R${:.2f}'.format(multa))
print('Tenha um bom dia. Dirija com segurança!!')