import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def kmeans(data: pd.DataFrame, nClusters=3, maxIters=300):
    centroids = data.sample(n=nClusters, replace=True).to_numpy()
    dists = [None for _ in range(0, nClusters)]
    assigned = np.random.randint(0, nClusters, data.shape[0])
    data = data.copy()

    print("Centroides iniciales")
    print(centroids)

    for _ in range(0, maxIters):
        oldCentroids = centroids.copy()
        for k in range(0, nClusters):
            dists[k] = np.sqrt((data.sub(centroids[k]).sum(axis=1)) ** 2)
        assigned = np.array(dists).argmin(axis=0)
        
        for k in range(0, nClusters):
            cluster = data[assigned == k]
            if (cluster.size == 0):
                continue

            centroids[k] = cluster.mean(axis=0)

        if (np.array_equal(oldCentroids, centroids)):
            print("Centroides convergen")
            break

    data["k"] = assigned
    return (data, centroids)