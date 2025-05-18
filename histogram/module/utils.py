from matplotlib import pyplot as plt

def plot_image(image_array, title):
    plt.imshow(image_array, cmap='gray')
    plt.title(title)
    plt.axis('on')
    # plt.show()

def grey_histogram(histogram):
    intensities = [item[0] for item in histogram]
    frequencies = [item[1] for item in histogram]
    plt.bar(intensities, frequencies, color='blue', alpha=0.7)
    plt.title('Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

def rgb_histogram(histograms):
    colors = ('b', 'g', 'r')
    for hist, color in zip(histograms, colors):
        plt.plot(hist, color=color)
    
    plt.xlim([0, 256])
    plt.title('Histogram RGB')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

# fungsi untuk menampilkan histogram grayscale
def plot_histogram_grey(histogram, image_array):
    """
    Plots the original image and its histogram side by side.
    """
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plot_image(image_array, 'Original Image')
    plt.subplot(1, 2, 2)
    grey_histogram(histogram)
    plt.tight_layout()
    plt.show()


# Fungsi untuk menampilkan histogram RGB
def plot_historgam_rgb(histogram, image_array):
    """
    Plots the original image and its histogram side by side.
    """
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plot_image(image_array, 'Original Image')
    plt.subplot(1, 2, 2)
    rgb_histogram(histogram)
    plt.tight_layout()
    plt.show()