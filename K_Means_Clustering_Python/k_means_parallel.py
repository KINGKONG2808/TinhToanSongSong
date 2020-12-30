import numpy as np
import cv2 as cv
import time


def K_Means(image, K):
    if len(image.shape) < 3:
        Z = image.reshape((-1, 1))
    elif len(image.shape) == 3:
        Z = image.reshape((-1, 3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    # Now convert back into unit8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    clustered_image = res.reshape(image.shape)

    return clustered_image


def main():
    start = time.time()
    input_image = cv.imread("test_image.png")
    # displaying input image
    # cv.imshow("input_image", input_image)
    # cv.waitKey(0)

    # n = int(input('Enter the cluster: '))
    clusters = 5
    clustered_image = K_Means(input_image, clusters)
    # displaying output image
    end = time.time()
    print(f'Calculator time parallel from start to end in: {end - start}')
    # cv.imshow("output_image", clustered_image)
    # cv.waitKey(0)

    cv.imwrite("cluster_image_parallel.png", clustered_image)


if __name__ == '__main__':
    main()
