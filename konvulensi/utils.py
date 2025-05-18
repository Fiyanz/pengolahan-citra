import numpy as np
from scipy.ndimage import median_filter

# menambahkkan 0 disetiap sisi matriks
def add_padding(matrix, padding):
    """
    Menambahkan padding pada matriks
    :param matrix: matriks yang akan ditambahkan padding
    :param padding: jumlah padding yang akan ditambahkan
    :return: matriks dengan padding
    """
    if padding == 0:
        return matrix

    # menambahkkan 0 disetiap sisi matriks
    return np.pad(matrix, ((padding, padding), (padding, padding)), mode='constant', constant_values=0)

# mengubah matriks menjadi biner dengan treshold
def to_binary(matrix, threshold):
    """
    Mengubah matriks menjadi biner dengan treshold
    :param matrix: matriks yang akan diubah
    :param threshold: treshold yang akan digunakan
    :return: matriks biner
    """
    return np.where(matrix > threshold, 1, 0)

# median filter

def median_fil(matrix, size=3, padding='constant'):
    if size % 2 == 0:
        raise ValueError("Ukuran jendela median harus ganjil.")
    matrix_np = np.array(matrix)
    return median_filter(matrix_np, size=size, mode=padding)
