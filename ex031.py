x = float(input('Qual foi a distância da viagem em km?  '))
if x>200:
    p = x*0.45
    print('\033[4;32mO preço da viagem será R${:.2f}\033[m'.format(p))
else:
    r = x*0.50
    print('\033[4;32mO preço da viagem será R${:.2f}\033[m'.format(r))