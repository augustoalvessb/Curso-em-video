d = float(input('Uma distancia em metros: '))
print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam'.format(d, (d / 1000), (d / 100), (d / 10)))
print('{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format((d * 10), (d * 100), (d*1000)))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('A medida de {}m corresponde a \n{}km \n{:.0f}hm \n{:.0f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(d, km, hm, dam, dm, cm, mm))

