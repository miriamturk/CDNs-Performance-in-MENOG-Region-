import matplotlib.pyplot as plt
from RTT import *

averages = totalAverage(directory)


proportions = []
labels = []
dico = {}

for d in averages.values():
    if d != {}:
        key_min = min(d, key=d.get)
        if key_min in dico.keys():
            dico[key_min]+= 1
        else:
            dico[key_min]=1
  
plt.figure()
patches, texts, autotexts = plt.pie(dico.values(),labels=dico.keys(),
                autopct=lambda p:'{:.2f}%  ({:,.0f})'.format(p,p*sum(dico.values())/100))
for i in autotexts:
    i.set_fontsize(8)

plt.title('CDNs success')
plt.savefig('pieplot.png')
plt.close()





