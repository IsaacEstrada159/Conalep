import random 
lista = ['A', 'C', 'T', 'G']
lista2 = []
repetidos = 0
for i in range(500):
  random.shuffle(lista)
  print(lista)
  if lista == ['A', 'C', 'T', 'G']:
    repetidos += 1
print('Repetidos', repetidos)
