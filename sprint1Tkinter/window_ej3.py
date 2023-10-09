import tkinter as tk
from yes_window import show_yes_window
from no_window import show_no_window
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blue label mejor Whiskie")


        yes_button = ttk.Button(self, text="Sí", command=show_yes_window)
        yes_button.pack(side="left")

        no_button = ttk.Button(self, text="No", command=show_no_window)
        no_button.pack(side="left")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()