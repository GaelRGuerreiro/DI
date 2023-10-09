#window.py
from tkinter import ttk
import tkinter as tk
from cell_ej5 import Cell
from tkinter import messagebox
from PIL import Image,ImageTk
 
class MainWindow:
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda"+cell.title
        messagebox.showinfo("Información", message)
    def __init__(self,root):
        root.title("MainWindow")
        self.cells = [
            Cell("Assasins Creed","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\edited\\creed1.jpg"),
            Cell("Assasins Creed 2","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\edited\\creed2.jpg"),
            Cell("Assasins Creed 3","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\edited\\creed3.jpg"),
            Cell("Assasins Creed Black Flag","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\edited\\creed4.jpg"),
            Cell("Assasins Creed Rogue","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\edited\\creed5.jpg"),
        ]
        for i, cell in enumerate(self.cells):
            cell.load_image()
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))