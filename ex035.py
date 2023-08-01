x = float(input('Digite o tamanho do primeiro segmento:  '))
y = float(input('Digite o tamanho do segundo segmento:  '))
z = float(input('Digite o tamanho do terceiro segmento:  '))
if x < y + z and y < x + z and z < x + y:
    print('\033[34mVocê formou um triângulo!\033[m')
else:
    print('\033[1;31mVocê não formou um triângulo\033[m')

