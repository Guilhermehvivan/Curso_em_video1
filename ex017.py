import math
b=float(input('Qual é o comprimento do cateto adjacente?'))
c=float(input('Qual é o comprimento do cateto oposto?'))
a=math.sqrt(b**2+c**2)
print('O triângulo retângulo terá uma hipotenusa medindo {}'.format(a))
