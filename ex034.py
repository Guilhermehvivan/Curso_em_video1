x = float(input('Qual é o seu salário?  '))
if x>1250:
    y = x + (x*10/100)
    print('\033[4;35mO novo salário será de R${:.2f}\033[m'.format(y))
else:
    z = x + (x*15/100)
    print('\033[4;35mO novo salário será de R${:.2f}\033[m'.format(z))