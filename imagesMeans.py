import matplotlib.pyplot as plt
import pandas as pd
from sys import argv

from src.kmeans import kmeans
from random import seed
from PIL import Image

def img_to_df(pixels):
    return pd.DataFrame(pixels, columns=["R","G","B"])

seed(5)
path = argv[1]
ks = int(argv[2])
its = int(argv[3])

im = Image.open(path)
imDf = img_to_df(list(im.getdata()))
imass, imcent = kmeans(imDf, ks, its)
impal = imass['k'].apply(lambda k: tuple(imcent[k])).to_numpy().reshape(im.size[1], im.size[0])

print("Centroides")
print(imcent)
    
for gn, gl in imass.groupby(["k"]):
    print(f'Asignados a centroide {tuple(imcent[gn[0]])}: {gl.shape[0]}')

plt.imshow(impal.tolist())
plt.savefig(f'im_k{ks}_its{its}.jpg')
plt.show()
