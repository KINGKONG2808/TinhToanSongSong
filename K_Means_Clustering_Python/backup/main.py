import k_means_parallel
from backup import k_means
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('-' * 50)
    print('\tDiff about K_Means \'Parallel\' vs \'Sequentially\'')
    print('\t1: K means clustering')
    print('\t2: K means sequentially')
    print('\t0: Exit program')
    print('-' * 50)
    n = -1
    while n != 0:
        n = int(input('- Enter your switch: '))
        cv.destroyAllWindows()
        plt.close('all')
        if n == 1:
            k_means_parallel.main()
            n = -1
        elif n == 2:
            k_means.main()
            n = -1
        else:
            print('Unkown your selected !')
            exit()
