x = float(input('Digite a velocidade do carro: '))
if x >= 80:
    print('Você foi multado')
    m = 7*(x-80)
    print('O valor da multa será {}'.format(m))
else:
    print('Sem multa')


