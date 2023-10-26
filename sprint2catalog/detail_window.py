#detail_window
import tkinter as tk
from tkinter import ttk

class DetailWindow:

    def __init__(self, root, title, descripcion,image):

        self.root = root
        self.title = title
        self.descripcion = descripcion
        self.image = image

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")


        self.window = tk.Toplevel(root)
        self.window.title(self.title)

        image_label = ttk.Label(self.window, image = self.image)
        image_label.pack()
        title_label = ttk.Label(self.window, text = self.title, font=("JetBrains mono", 16))
        title_label.pack()
        descripcion_label = ttk.Label(self.window, text = self.descripcion, wraplength = 300)
        descripcion_label.pack()