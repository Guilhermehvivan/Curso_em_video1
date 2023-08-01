n=str(input('Digite seu nome completo:  '))
print('Seu nome em letras maiúsculas é {}'.format(n.upper()))
print('Seu nome em letras maiúsculas é {}'.format(n.lower()))
x=n.strip()
print('Seu nome tem ao todo {} letras'.format(len(x)-n.count(' ')))
y=x.split()
print('Seu primeiro nome possui {} letras'.format(len(y[0])))





