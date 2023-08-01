import random
x=str(input('Primeiro aluno: '))
y=str(input('Segundo aluno: '))
w=str(input('Terceiro aluno: '))
z=str(input('Quarto aluno: '))
lista= [x, y, w, z]
random.shuffle(lista)
print('A ordem dos alunos será {}'.format(lista))