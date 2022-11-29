import pandas as pd
import random
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
lista = [1,2,3,4,5,6]
tamaño = 300000
lista2 = []
for i in range(tamaño):
 lista2.append(random.choice(lista) + random.choice(lista))
df = pd.DataFrame(lista2)
df2 = df.mean()
for j in range(1,7):
  df2 = (j/6)/df
  df2 = df2.mean()
  print(df2)
df2 =stats.norm(scale=1, loc=0).rvs(1000)
ax = sns.distplot(df2,
                  bins=6,
                  kde=True,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()
