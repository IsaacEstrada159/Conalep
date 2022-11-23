import random
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
replicas = #"ultimos seis o siete números de tu matricula"
repetidos = 0
iguales = []
lista = []
outputs = []
for i in range(replicas):
    char_length = 10
    char_length2 = 10
    char_length3 = 10
    genoma1 = ["A", "C", "T", "G"]
    genoma2 = ["A", "C", "T", "G"]
    genoma3 = ["A", "C", "T", "G"]
    output = []
    output2 = []
    output3 = []
    for j in range(char_length):
        selection = random.choice(genoma1)
        selection2 = random.choice(genoma2)
        selection3 = random.choice(genoma3)
        output.append(selection)
        output2.append(selection2)
        output3.append(selection3)
    output_1 = "".join(output)
    output_2= "".join(output2)
    output_3= "".join(output3)
    #print(i, output_1,';',output_2, ';', output_3 )
    if output_1[0:3] == output_2[0:3] == output_3[0:3]:
      repetidos += 1
      if repetidos >= 1:
        iguales.append(i)
        output_1a = outputs.append(output_1)
        output_2a = str(output_2)
        output_3a = str(output_3)
        print('____', i ,output_1,';',output_2, ';', output_3)
for z in range(len(iguales)):
  lista.append(z)
y = outputs
x = lista
print('Repetidos:',repetidos, 'Promedio',(repetidos*10)/replicas,'%' )
sizes = np.random.uniform(80, 80, len(x))
colors = np.random.uniform(50, 80, len(x))
fig, ax = plt.subplots()
plt.title("ADN")
ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
plt.ylabel('genomas')
plt.xlabel('posición')
plt.title('Genomas repetidos')

plt.show()
