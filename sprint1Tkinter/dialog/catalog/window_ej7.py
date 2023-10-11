#window.py
from tkinter import ttk
import tkinter as tk
from cell_ej7 import Cell
from tkinter import messagebox
from PIL import Image,ImageTk
from detail_window import DetailWindow
 
class MainWindow:
    def on_button_clicked(self, cell):
         detail_window = DetailWindow(self.root, cell.title, cell.image_tk, cell.description)

    def __init__(self,root):
        self.root=root
        root.title("Primeros 5 juegos de Assassins Creed")
        self.cells = [
            Cell("Assasins Creed","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\unedited\\creed1.jpg","Eres un Assassin que acecha a su presa con una hoja oculta. Un guerrero envuelto en el misterio y temido por su crueldad. Tus acciones pueden sembrar el caos en tu entorno inmediato, y tu propia existencia determinará los acontecimientos futuros durante este momento crucial de la historia."),
            Cell("Assasins Creed 2","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\unedited\\creed2.jpg","Assassin's Creed II presenta a Ezio, un nuevo Assassin que continúa el legado letal de sus antepasados. Enfréntate a una historia épica de poder y corrupción en la que pulirás tu artes de Assassin, y empuñarás armas e instrumentos diseñados por el mismísimo Leonardo da Vinci en esta continuación de la serie apasionante y mortal."),
            Cell("Assasins Creed 3","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\unedited\\creed3.jpg","1775: Las colonias americanas van a iniciar una rebelión. En la piel de Connor, un Assassin nativo americano, lucha por la libertad de tu nación. Asesina a tus enemigos con estilos diferentes y una enorme variedad de armas en entornos que van desde las bulliciosas calles de la gran ciudad hasta el caos del campo de batalla."),
            Cell("Assasins Creed Black Flag","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\unedited\\creed4.jpg","Assassin's Creed IV Black Flag comienza en 1715, cuando los piratas establecieron una república sin ley en el Caribe y dominaron la tierra y el mar. Estos forajidos paralizaban navíos, interrumpían el comercio internacional y saqueaban vastas fortunas. Pusieron en peligro las estructuras de poder que gobernaban Europa, desataron la imaginación de millones de personas y dejaron un legado que aún perdura."),
            Cell("Assasins Creed Rogue","C:\\msys64\\home\\gaelr\\DI\\sprint1Tkinter\\dialog\\catalog\\unedited\\creed5.jpg","Contempla la transformación de Shay, de Assassin aventurero a lúgubre templario convencido dispuesto a cazar a sus antiguos hermanos. Vive en primera persona los sucesos que llevarán a Shay hacia una senda oscura que cambiará para siempre el destino de la Hermandad."),
        ]
        for i, cell in enumerate(self.cells):
            cell.load_image()
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))