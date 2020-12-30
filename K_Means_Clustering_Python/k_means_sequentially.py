from skimage import io
from sklearn.cluster import KMeans
import numpy as np
import time


def sequentially():
    start = time.time()
    # reading the image
    image = io.imread('test_image.png')
    io.imshow(image)
    # preprocessing
    rows, cols = image.shape[0], image.shape[1]
    image = image.reshape(rows * cols, 3)
    # print(image.shape)
    # print(image[:5])
    k = 5
    kMeans = KMeans(n_clusters=k)
    kMeans.fit(image)

    # centers
    centers = np.asarray(kMeans.cluster_centers_, dtype=np.uint8)
    # labels
    labels = np.asarray(kMeans.labels_, dtype=np.uint8)
    # print(labels.shape)
    labels = np.reshape(labels, (rows, cols))
    # print(labels.shape)

    newImage = np.zeros((rows, cols, 3), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            # assinging every pixel the rgb color of their label's center
            newImage[i, j, :] = centers[labels[i, j], :]
    io.imsave('cluster_image_sequentially.png', newImage)

    io.imshow(newImage)
    end = time.time()
    print(f'Calculator time sequentially from start to end in: {end - start}')


if __name__ == '__main__':
    sequentially()
