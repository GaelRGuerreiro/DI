from PIL import Image, ImageTk
import tkinter as tk

class Cell:
    def __init__(self, title, path):
        self.title = title
        self.path = path
        self.image_tk = None
    def load_image(self):
        try:
            image = Image.open(self.path)
            #Reescalar imagen
            image =image.resize((100, 100), Image.Resampling.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(image)
        except Exception as e:
            print("Error cargando la imagen:", e)