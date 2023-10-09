import tkinter as tk

def show_no_window():
    no_root = tk.Tk()
    no_root.title("No Window")

    def on_button_click():
        # Acción a realizar cuando se hace clic en el botón
        pass

    button = tk.Button(no_root, text="No eres un verdadero whisky lover", command=on_button_click)
    button.pack()

    no_root.mainloop()

if __name__ == "__main__":
    show_no_window()