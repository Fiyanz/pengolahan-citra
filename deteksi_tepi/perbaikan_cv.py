import cv2
import numpy as np

def histogram_equalization(img):
    # Asumsi input adalah citra grayscale
    h, w = img.shape
    n = h * w           # Jumlah total piksel
    L = 256             # Jumlah level intensitas untuk 8-bit

    # Hitung histogram
    hist = np.zeros(L, dtype=int)
    for value in img.flatten():
        hist[value] += 1

    # Hitung histogram kumulatif
    cum_hist = np.cumsum(hist)

    # Hitung nilai transformasi untuk setiap level k
    sk = ((L - 1) / n) * cum_hist
    sk = sk.astype(np.uint8)  # Konversi ke uint8

    # Terapkan transformasi ke citra asli
    equalized_img = sk[img]

    return equalized_img



if __name__ == "__main__":
    # Baca gambar dalam grayscale
    # image = [
    #     [0, 0, 0, 0, 0],
    #     [0, 1, 1, 1, 0],
    #     [0, 1, 2, 1, 0],
    #     [0, 1, 1, 1, 0],
    #     [0, 0, 0, 0, 0]
    # ]
    image = [
        [6, 6, 2, 2, 7, 7,  ],
        [6, 6, 5, 5, 7, 6,  ],
        [6, 0, 1, 1, 2, 2,  ],
        [7, 0, 1, 0, 2, 2,  ],
        [3, 0, 1, 0, 4, 2,  ],
        [6, 6, 3, 6, 1, 2,  ] 
    ]

    image = np.array(image)

    # Terapkan histogram equalization manual
    result = histogram_equalization(image)
    print(result)
