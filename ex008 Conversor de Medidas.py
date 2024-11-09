metros = float(input('Digite a distancia em metros:'))
#km hm dam m dm cm mm
mm = metros * 1000
cm = metros * 100
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('A media de {}m corresponde a: \n{:.0f}mm \n{:.0f}cm \n{:.0f}dm \n{:}dam \n{:}hm \n{:}km'.format(metros, mm, cm, dm, dam, hm, km))
