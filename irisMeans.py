import matplotlib.pyplot as plt
import pandas as pd

from src.utils import get_color_gradient
from src.kmeans import kmeans
from random import seed
from sys import argv

seed(5)
ks = int(argv[1])
its = int(argv[2])

irisDf = pd.read_csv('iris.csv', engine='c').drop("species", axis=1)
imass, icent = kmeans(irisDf, ks, its)

print("Centroides")
print(icent)
    
for gn, gl in imass.groupby(["k"]):
    print(f'Asignados a centroide {tuple(icent[gn[0]])}: {gl.shape[0]}')

colGrad = get_color_gradient("FF0000", "00FFFF", ks)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(imass.iloc[:,0], imass.iloc[:,1], imass.iloc[:,2], c=[colGrad[i] for i in imass["k"]], s=imass.iloc[:,3]*10)
ax.scatter(icent[:,0], icent[:,1], icent[:,2], s=icent[:,3]*10, c="black", marker="x")
plt.savefig(f'iris_k{ks}_its{its}.jpg')
plt.show()