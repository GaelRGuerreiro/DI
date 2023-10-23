import threading
import requests
import tkinter as tk

class LoadWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")
        self.canvas = tk.Canvas(self.root, width=50, height=50, bg=label_bg_color)
        self.canvas.pack()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
    

        self.progress = 1

        self.draw_progress_circle(self.progress)
        self.update_progress_circle()

        



    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100)) 

        self.canvas.create_arc(10, 10, 40, 40,
                               start=0, extent=angle+10, tags="progress", outline='green', width=6, style=tk.ARC)

    def update_progress_circle(self):
        self.progress += 4  
             
        self.draw_progress_circle(self.progress)

        self.root.after(50, self.update_progress_circle)

    




    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/GaelRGuerreiro/DI/main/catalog.json")       
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
            print(response.json()) 


    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)




def launch_main_window(json_data):
    root=tk.Tk()
    app=LoadWindow(root,json_data)
    root.mainloop

    





