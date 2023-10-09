import tkinter as tk

def show_yes_window():
    yes_root = tk.Tk()
    yes_root.title("Yes Window")

    def on_button_click():
      
        pass

    button = tk.Button(yes_root, text="Blue label de Jhonie Walker un elisir.", command=on_button_click)
    button.pack()

    yes_root.mainloop()