import numpy as np
from konvulensi import konvolusi, konvolusi_2x2
from utils import to_binary, median_fil, add_padding, citra_negative
from kernel import Kernel

# Menghitung prewitt dari matriks
def prewitt(matrix, kernel, treshold):
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
    # print(prewit)
    prewit = to_binary(prewit, treshold)
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
    print(mean)

# deteksi tepi roberts 
def roberts(matrix, kernelx=None, kernely=None, treshold=0):

    gx = konvolusi(matrix, kernelx)
    gy = konvolusi(matrix, kernely)

    result = abs(gx) + abs(gy)
    result = to_binary(result, treshold)
    print(result)



if __name__ == "__main__":

    array = [
        [219,  99,  15,  27,  87,  57, 142,  98, 126],
        [184, 103, 188, 137,  63, 241,  63,  51, 198],
        [109, 133, 227, 229, 214, 222,  14,  20,  95],
        [224, 203, 200,  96, 145,  81, 224, 147, 143],
        [181,  20, 157, 251, 133, 201, 247, 164, 230],
        [145,  99, 205,  78, 231, 137,  55,  74,  90],
        [207, 184, 209,  99, 196, 189, 174, 195, 135],
        [ 13, 137,  24, 235, 178, 142, 123, 254, 102],
        [181, 162, 209, 102, 120,  12, 178, 216,  89]
    ]

    print(array[3][2])
    print(citra_negative(array))

    # print("Median Filter")
    # print(median_fil(matrix=array, padding='constant'))
    # print("Prewitt")
    # prewitt(array, Kernel.PREWITT, 130)
    # # print("Roberts")
    # # roberts(array, Kernel.ROBERTS_X, Kernel.ROBERTS_Y)
    # print("roberts biner")
    # print(roberts(array, Kernel.ROBERTS_X, Kernel.ROBERTS_Y, 130))

