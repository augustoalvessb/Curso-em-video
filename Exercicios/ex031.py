'''km = float(input('Qual a distancia da sua viagem? '))
print('Você esta preste a começar uma viagem de {}km'.format(km))
menos = km * 0.50
mais = km * 0.45
if km < 201 :
    print('E o preço da passagem é R${:.2f}'.format(menos))
else:
    print('E o preço da passagem é R${:.2f}'.format(mais))

km = float(input('Qual a distancia da sua viagem?' ))
print('Você esta preste a começar uma viagem de {}km.'.format(km))
if km > 200 :
    print('o preço da passagem é R${:.2f}'.format(km * 0.45))
else:
    print('O preço da passagem é R${:.2f}'.format(km * 0.50))'''

km = float(input('Qual a distancia da usa viagem? '))
print('Você esta prestes a começar uma viagem de {}km'.format(km))
preço = km * 0.50 if km <= 200 else km * 0.45
print('O preço da passagem é R${:.2f}'.format(preço))
