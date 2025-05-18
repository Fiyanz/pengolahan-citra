import numpy as np
import cv2 as cv

# fungsi untuk image grayscale
def image_grayscale(image_path):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    return image

# fungsi untuk image rgb
def image_rgb(image_path):
    image = cv.imread(image_path, cv.IMREAD_COLOR_RGB)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    return image

# fungsi untuk image biner
def image_binary(image_path, treshold=127):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    _, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
    return binary_image


# fungsi untuk mendapatkan shape image
def get_shape(image_path):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    return image.shape