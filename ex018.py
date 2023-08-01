import math
x=float(input('Digite um ângulo: '))
a=math.radians(x)
b=math.sin(a)
c=math.cos(a)
d=math.tan(a)
print('O ângulo {} tem seno {}, cosseno {} e tangente {}'.format(x,b,c,d))