import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk
from cell import Cell
from detail_window import DetailWindow
from tkinter import messagebox, Canvas, Scrollbar, Frame, Label

# Función que devuelve la imagen de cada item del JSON
def load_image_from_url(url, width, height):
    response = requests.get(url)
    image_data = Image.open(BytesIO(response.content))
    image = image_data.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

def acerca_de():
    info = "Este desarrollador es un profesional."
    messagebox.showinfo("Acerca del desarrollador:", info)

class MainWindow():
    def on_button_clicked(self, name, descripcion, image):
        detail_window = DetailWindow(self.root, name, descripcion, image)

    def __init__(self, root, json_data):
        self.root = root
        root.title("MainWindow")
        self.cells = []

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        # Crear el Canvas y el Scrollbar
        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)

        # Crear el Frame que será desplazable
        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Agregar Canvas y Scrollbar a la ventana
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        labels = []

        # Bucle para recorrer todos los items del JSON descargado y añadirlos al Frame
        for item in json_data:
            name = item["name"]
            descripcion = item["descripcion"]
            image_url = item["image_url"]
            image = load_image_from_url(image_url, 200, 200)

            cell = Cell(name, descripcion, image_url, image)
            self.cells.append(cell)

            # Creación de etiquetas en el Frame
            label = Label(self.scrollable_frame, image=cell.image, text=name, compound=tk.BOTTOM)
            label.grid(row=len(labels), column=0)
            label.bind("<Button-1>", lambda event, cell=cell, name=name, descripcion=descripcion, image=image: self.on_button_clicked(name, descripcion, image))
            labels.append(label)