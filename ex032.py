x = int(input('Digite um ano:  '))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('\033[1;31mEsse ano é bissexto!\033[m')
else:
    print('\033[1;31mEsse ano não é bissexto\033[m')