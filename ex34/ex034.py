sal = float(input('Qual salario do funcionario? R$'))
if sal <= 1250:
    print('O seu aumento será de R${:.2f}'.format(sal * (15 / 100) + sal ))
else:
    print('Seu aumento será de R${:.2f}'.format(sal * (10/100) + sal))
#PARA CALCULAR DESCONTO É SO TROCAR O 'SAL+' POR 'SAL-'

#forma GUANABARA
'''salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))'''
