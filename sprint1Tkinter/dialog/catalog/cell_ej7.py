import tkinter as tk
from PIL import Image, ImageTk

class Cell:

    def __init__(self, title, path, description):

        self.title = title
        self.path = path
        self.description = description
        self.load_image()

        
    def load_image(self):
        try:
            image = Image.open(self.path)
            resized_image = image.resize((100, 100), Image.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            print("Error cargando la imagen:", e)
      #  resizedImage = (Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS)
       # self.imageTk = ImageTk.PhotoImage(resizedImage)
       