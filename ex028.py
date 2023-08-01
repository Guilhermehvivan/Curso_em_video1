import random
import time
x = int(input('Digite um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
y = random.choice(lista)
print('Processando...')
time.sleep(2)
print('O computador escolheu {}'.format(y))
if x == y:
    print('Você acertou!')
else:
    print('Você perdeu!')
