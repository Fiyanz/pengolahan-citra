def hitung_histogram(image, L=256):
    histogram = [0] * L
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram

def hitung_histogram_kumulatif(histogram):
    cumulative_hist = [0] * len(histogram)
    cumulative_hist[0] = histogram[0]
    for i in range(1, len(histogram)):
        cumulative_hist[i] = cumulative_hist[i - 1] + histogram[i]
    return cumulative_hist

def hitung_transformasi(cumulative_hist, total_pixels, L=256):
    sk = [0] * len(cumulative_hist)
    for k in range(len(cumulative_hist)):
        sk[k] = int((L - 1) * cumulative_hist[k] / total_pixels)
    return sk

def terapkan_transformasi(image, sk):
    new_image = []
    for row in image:
        new_row = [sk[pixel] for pixel in row]
        new_image.append(new_row)
    return new_image

def histogram_equalization_manual(image, L=256):
    height = len(image)
    width = len(image[0])
    total_pixels = height * width

    hist = hitung_histogram(image, L)
    cum_hist = hitung_histogram_kumulatif(hist)
    sk = hitung_transformasi(cum_hist, total_pixels, L)
    new_image = terapkan_transformasi(image, sk)

    return new_image



if __name__ == "__main__":
    # Contoh penggunaan
    image = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 2, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    image = [
        [6, 6, 2, 2, 7, 7,  ],
        [6, 6, 5, 5, 7, 6,  ],
        [6, 0, 1, 1, 2, 2,  ],
        [7, 0, 1, 0, 2, 2,  ],
        [3, 0, 1, 0, 4, 2,  ],
        [6, 6, 3, 6, 1, 2,  ]
    ]


    new_image = histogram_equalization_manual(image)
    print("Gambar setelah histogram equalization:")
    for row in new_image:
        print(row)