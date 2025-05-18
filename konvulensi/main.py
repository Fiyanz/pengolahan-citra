import numpy as np
from konvulensi import konvolusi
from utils import to_binary, median_fil
from kernel import Kernel

# Menghitung prewitt dari matriks
def prewitt(matrix, kernel):
    """
    Menghitung prewitt dari matriks
    :param matrix: matriks yang akan dihitung prewitt
    :param kernel: kernel yang akan digunakan
    :return: matriks prewitt
    """
    # Ubah ke array numpy
    matrix = np.array(matrix)
    kernel = np.array(kernel)

    gx = konvolusi(matrix, kernel, padding=1)
    gy = konvolusi(matrix, kernel.T, padding=1)

    prewit = abs(gx) + abs(gy)
    prewit = to_binary(prewit, 100)
    print(prewit)

# mean filter
def mean_filter(matrix, kernel):
    """
    Menghitung mean filter dari matriks
    :param matrix: matriks yang akan dihitung mean filter
    :param kernel: kernel yang akan digunakan
    :return: matriks mean filter
    """
    # Ubah ke array numpy
    matrix = np.array(matrix)
    kernel = np.array(kernel)

    mean = konvolusi(matrix, kernel, padding=1)
    mean = mean / 9
    # short 
    return mean



if __name__ == "__main__":
    matrix1 = [
        [42, 42, 30, 31, 35, 43],
        [25, 11, 3,  31, 42, 33],
        [54, 30, 12, 61, 37, 42],
        [32, 56, 29, 30, 17, 20],
        [48, 39, 53, 22, 19, 23],
        [23, 20, 31, 60, 30, 37]
    ]

    matrix2 = [
            [196,  54,  18, 176, 195,  44],
            [ 29, 212, 133,  40, 129, 239],
            [182, 247,  46, 153, 254,  33],
            [  5, 161, 167, 198,   0,  96],
            [216,  21, 124,  54,  18, 254],
            [244,  41,  94, 175,  25,  75]
        ]

    print("Median Filter")
    print(median_fil(matrix=matrix2, padding='constant'))
    print("Prewitt")
    print(prewitt(matrix1, Kernel.PREWITT))