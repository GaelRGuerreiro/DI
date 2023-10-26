import threading
import requests
from tkinter import Tk
import tkinter as tk
from window import MainWindow  

class LoadWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")  
        self.root.geometry("170x120")  
        self.root.resizable(False, False)  
        self.finished = False 
        self.json_data = []  
        self.progress = 0  # 

        # Calcula la posición central de la ventana
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")


        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 12))
        self.label.pack()

        label_bg_color = self.label.cget("bg")

        # Crea un lienzo para mostrar una animación 
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

       
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()  

      
        self.check_thread()


        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

    def draw_progress_circle(self, progress):

        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10, 10, 40, 40,
                               start=0, extent=angle + 10, tags="progress", outline='green', width=6, style=tk.ARC)

    def update_progress_circle(self):

        self.progress += 4
        self.draw_progress_circle(self.progress)


        self.root.after(50, self.update_progress_circle)

    def fetch_json_data(self):
        # Descarga datos desde GitHub
        response = requests.get("https://raw.githubusercontent.com/GaelRGuerreiro/DI/main/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json() 
            self.finished = True 
            print(response.json())

    def check_thread(self):
        # Comprueba si la carga ha finalizado y destruye la ventana de carga
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)  
        else:
            
            self.root.after(100, self.check_thread)

def launch_main_window(json_data):
    # Función para lanzar la ventana principal con los datos descargados
    root = Tk()
    app = MainWindow(root, json_data)
    root.mainloop()





