import random
import time
print('-°-°'*15)
print('Vou pensar em um núemro de 0 a 5. Tente adivinhar...')
print('-°-°'*15)
pc = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
time.sleep(1)
n = random.choice([0, 1, 2, 3, 4, 5]) # FAZ O PC PENSAR
if pc == n:
    print('PARABÉNS, VOCÊ ME VENCEU!!')
else:
    print("YOU LOSE. Eu pensei no número {} não no {}".format(n, pc))