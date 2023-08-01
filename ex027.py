x = str(input('Digite seu nome: ')).strip()
y = x.split()
print('O seu primeiro nome é {}'.format(y[0]))
print('Seu último nome é {}'.format(y[len(y)-1]))
