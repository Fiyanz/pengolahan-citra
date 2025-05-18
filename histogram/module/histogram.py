import cv2 as cv

# fungsi histogram manual
def histogram(frequency, pixel):
    histogram = []
    for itensits, freq in frequency:
        freqRelative = freq / pixel
        histogram.append([itensits, freq, freqRelative])
    return histogram

# Fungsi untuk menghitung histogram RGB
def histogram_rgb(image):
    histograms = []
    for i in range(3):  # 0=Blue, 1=Green, 2=Red
        histr = cv.calcHist([image], [i], None, [256], [0, 256])
        histograms.append(histr)
    return histograms