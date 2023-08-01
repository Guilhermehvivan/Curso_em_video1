x = float(input('Digite o primeiro número:  '))
y = float(input('Digite o segundo número:  '))
z = float(input('Digite o terceiro número:  '))
if x > y > z:
    print('O maior número é {} e o menor é {}'.format(x, z))
if x > z > y:
    print('O maior número é {} e o menor é {}'.format(x, y))
if y > z > x:
    print('O maior número é {} e o menor é {}'.format(y, x))
if y > x > z:
    print('O maior número é {} e o menor é {}'.format(y, z))
if z > x > y:
    print('O maior número é {} e o menor é {}'.format(z, y))
if z > y > x:
    print('O maior número é {} e o menor é {}'.format(z, x))