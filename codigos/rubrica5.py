import random

replicas = 3000000
repetidos = 0
iguales = []
for i in range(replicas):
    char_length = 3
    char_length2 = 3
    char_length3 = 3
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
        print('____________', i ,output_1,';',output_2, ';', output_3)
      
print(repetidos, 'promedio',(repetidos*10)/replicas,'%' )
