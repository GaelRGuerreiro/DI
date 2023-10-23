#main.py
from tkinter import Tk
from ventana_de_carga import LoadWindow
 
if __name__ == "__main__":
    root = Tk()
    app = LoadWindow(root)
    root.mainloop()
 