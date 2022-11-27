import numpy as np
from sklearn.cluster import KMeans
from PIL import Image


class ColorExtractor:

    def extract_colors(self, filename):
        my_img = Image.open(filename[1:])
        img_array = np.array(my_img)
        clt = KMeans(n_clusters=10)
        clt.fit(img_array.reshape(-1, 3))
        return clt.cluster_centers_


