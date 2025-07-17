import tkinter as tk
from tkinter import ttk
from custom_style import CustomStyle

class SetupFrame(ttk.Frame):
    '''Frame to setup the underwater hockey game.
    Collects various inputs from the user, e.g. time, teams'''

    def __init__(self, master: tk.Tk | ttk.Frame) -> None:
        '''Create setup frame'''
        super().__init__(master) # Inherit methods from ttk.Frame

        self.style = CustomStyle(self)
        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure([0, 1], weight=1)

        info_lbl = ttk.Label(self, text="Enter game length (minutes)")
        info_lbl.grid(row=0, column=0, columnspan=2, sticky="NSWE", padx=5,
                      pady=5)
        
        total_lbl = ttk.Label(self, text="Total Game Length: ")
        total_lbl.grid(row=1, column=0, columnspan=2, sticky="NSWE", padx=5,
                      pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Setup")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    setup = SetupFrame(root)
    setup.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()
