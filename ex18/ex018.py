import math
an = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, sen))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tg))

from math import radians, sin, cos, tan
an = float(input('Digite o valor do ângulo: '))
sen = sin(radians(an))
print('O angulo de {} tem seno{:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O angulo de {} tem o cosseno {:.2f}'.format(an , cos))
tg = tan(radians(an))
print('O angulo de {} tem a tangente{:.2f}'.format(an, tg))


