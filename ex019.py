import random
x=str(input('Primeiro aluno: '))
y=str(input('Segundo aluno: '))
w=str(input('Terceiro aluno: '))
z=str(input('Quarto aluno: '))
lista= [x, y, w, z]
s=random.choice(lista)
print('O aluno sorteado será o {}'.format(s))
