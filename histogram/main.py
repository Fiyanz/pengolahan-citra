import tkinter as tk
import os
from module.histogram import histogram_rgb, histogram
from module.frequency import get_frequency2d
from module.utils import plot_histogram_grey, plot_historgam_rgb
from module.gui import ImageHistogramApp
from module.image import image_grayscale, image_rgb, image_binary   


def main_histtogram():
    # Path to the image file
    image_path = os.path.join(os.path.dirname(__file__), 'assets', 'Lenna.png')

    # histogram Grey
    image_gray = image_grayscale(image_path) # gray image
    frequency = get_frequency2d(image_gray) # get frequency of image
    histogram_result = histogram(frequency, image_gray.size) # get histogram of image
    plot_histogram_grey(histogram_result, image_gray) # plot histogram

    # histogram RGB
    img_rgb = image_rgb(image_path)
    result_histogram_rgb = histogram_rgb(img_rgb)
    plot_historgam_rgb(result_histogram_rgb, img_rgb)

# def main_gui():
#     # gui
#     root = tk.Tk()
#     app = ImageHistogramApp(root)
#     root.mainloop()

# def main_matriks():
#     array = [[6, 6, 2, 2, 7, 7],
#              [6, 6, 5, 5, 7, 6],
#              [6, 0, 1, 1, 7, 6],
#              [7, 0, 1, 0, 2, 2],
#              [3, 0, 1, 0, 4, 2],
#              [6, 6, 3, 6, 1, 2]]
    
    

    # frequency = get_frequency2d(array)
    # histogram_result = histogram(frequency, (8*8))
    # print(histogram_result)

if __name__ == '__main__':
    main_histtogram()
    # main_gui()
    # main_matriks()