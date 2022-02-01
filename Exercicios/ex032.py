'''import calendar
ano = int(input('Digite o ano que deseja analisar: '))
ano6 = calendar.isleap(ano)
if ano6 is True:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')'''
from datetime import date
ano = int(input('Digite o ano que deseja analisar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))