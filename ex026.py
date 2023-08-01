x = str(input('Digite uma frase: ')).lower().strip()
print('A frase possui {} letras a'.format(x.count('a')))
print('O primeiro a da frase está na posição {}'.format(x.find('a')+1))
print('O último a da frase está na posição {}'.format(x.rfind('a')+1))