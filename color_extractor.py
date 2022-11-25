import os

import numpy as np
from sklearn.cluster import KMeans
from PIL import Image


class ColorExtractor:

    def extract_colors(self, filename):
        my_img = Image.open(filename[1:])
        img_array = np.array(my_img)
        clt = KMeans(n_clusters=10)
        clt.fit(img_array.reshape(-1, 3))
        palette = self.palette(clt)
        print(palette)
        return palette[0]

    def palette(self, clusters):
        width = 300
        palette = np.zeros((50, width, 3), np.uint8)
        steps = width / clusters.cluster_centers_.shape[0]
        for idx, centers in enumerate(clusters.cluster_centers_):
            palette[:, int(idx * steps):(int((idx + 1) * steps)), :] = centers
        palette = np.unique(palette, axis=1)
        palette = np.unique(palette, axis=0)
        return palette