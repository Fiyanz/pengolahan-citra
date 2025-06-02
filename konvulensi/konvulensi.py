import numpy as np


def konvolusi(matrix, kernel, padding=0, stride=1):
    # Ubah ke array numpy
    matrix = np.array(matrix)
    kernel = np.array(kernel)
    
    # Ambil ukuran matrix dan kernel
    m_rows, m_cols = matrix.shape
    k_rows, k_cols = kernel.shape

    # Tambahkan padding
    if padding > 0:
        matrix = np.pad(matrix, ((padding, padding), (padding, padding)), mode='constant')

    # Hitung dimensi output
    out_rows = ((matrix.shape[0] - k_rows) // stride) + 1
    out_cols = ((matrix.shape[1] - k_cols) // stride) + 1

    # Buat array output
    output = np.zeros((out_rows, out_cols), dtype=int)

    # Lakukan konvolusi
    for i in range(0, out_rows):
        for j in range(0, out_cols):
            region = matrix[i*stride:i*stride + k_rows, j*stride:j*stride + k_cols]
            output[i, j] = np.sum(region * kernel)

    return output


#konvolusi menggunakan kernel 2x2
def konvolusi_2x2(matrix, kernel, padding=0, stride=1):
    # Ubah ke array numpy
    matrix = np.array(matrix)
    kernel = np.array(kernel)
    
    # Ambil ukuran matrix dan kernel
    m_rows, m_cols = matrix.shape
    k_rows, k_cols = kernel.shape

    # Tambahkan padding
    if padding > 0:
        matrix = np.pad(matrix, ((padding, padding), (padding, padding)), mode='constant')

    # Hitung dimensi output
    out_rows = ((matrix.shape[0] - k_rows) // stride) + 1
    out_cols = ((matrix.shape[1] - k_cols) // stride) + 1

    # Buat array output
    output = np.zeros((out_rows, out_cols), dtype=int)

    # Lakukan konvolusi
    for i in range(0, out_rows):
        for j in range(0, out_cols):
            region = matrix[i*stride:i*stride + k_rows, j*stride:j*stride + k_cols]
            output[i, j] = np.sum(region * kernel)

    return output