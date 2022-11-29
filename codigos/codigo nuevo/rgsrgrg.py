import pandas as pd
import random
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
lista = [1,2,3,4,5,6]
tamaño = 100000
lista2 = []
lista3 = []
for i in range(tamaño):
 lista2.append(random.choice(lista) + random.choice(lista))
df = pd.DataFrame(lista2)
df2 = pd.DataFrame(df)
for j in range(1,7):
  df2 = (j/6)/df
  df2 = df2.mean()
  lista3.append(df2)

data = {'probabilidades': ['dos','tres','cuatro','cinco','seis', 'siete'],'datos': lista3}
df3 = pd.DataFrame(data)
print(df3)
