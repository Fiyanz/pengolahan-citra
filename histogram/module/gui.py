import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from module.frequency import get_frequency2d
from module.histogram import histogram, histogram_rgb
from module.image import image_grayscale, image_rgb, image_binary

class ImageHistogramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image and Histogram Viewer")
        self.root.geometry("1024x600")

        # Create a frame for the plots
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create matplotlib figures for image and histogram
        self.fig, (self.ax_image, self.ax_histogram) = plt.subplots(1, 2, figsize=(8, 4))
        self.ax_image.set_title("Image")
        self.ax_image.axis("off")
        self.ax_histogram.set_title("Histogram")
        self.ax_histogram.set_xlabel("Pixel Intensity")
        self.ax_histogram.set_ylabel("Frequency")

        # Embed the matplotlib figure in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a button to select and process an image
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.select_button = tk.Button(
            self.button_frame,
            text="Select and Process Image",
            command=self.select_and_process_image,
            width=25,
            height=2
        )
        self.select_button.pack(pady=10)

    def select_and_process_image(self):
        """
        Opens a file dialog to select an image, processes it, and updates the plots.
        """
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )

        if not file_path:
            print("No file selected.")
            return

        # Load the selected image in grayscale
        image_array = image_grayscale(file_path)
        if image_array is None:
            print("Failed to load the image.")
            return

        # Process the image to calculate the histogram
        frequency = get_frequency2d(image_array)
        histogram_result = histogram(frequency, image_array.size)

        # Update the image plot
        self.ax_image.clear()
        self.ax_image.imshow(image_array, cmap="gray")
        self.ax_image.set_title("Image")
        self.ax_image.axis("off")

        # Update the histogram plot
        self.ax_histogram.clear()
        intensities = [item[0] for item in histogram_result]
        frequencies = [item[1] for item in histogram_result]
        self.ax_histogram.bar(intensities, frequencies, color="blue", alpha=0.7)
        self.ax_histogram.set_title("Histogram")
        self.ax_histogram.set_xlabel("Pixel Intensity")
        self.ax_histogram.set_ylabel("Frequency")

        # Redraw the canvas
        self.canvas.draw()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ImageHistogramApp(root)
#     root.mainloop()