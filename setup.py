import tkinter as tk
from tkinter import ttk
from custom_style import CustomStyle
from widgets.int_entry import IntEntry

class SetupFrame(ttk.Frame):
    '''Frame to setup the underwater hockey game.
    Collects various inputs from the user, e.g. time, teams'''

    def __init__(self, master: tk.Tk | ttk.Frame) -> None:
        '''Create setup frame'''
        super().__init__(master) # Inherit methods from ttk.Frame

        self.style = CustomStyle(self)
        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure([0, 1], weight=1)
        self.pad = 5

        self.info_lbl = ttk.Label(self, text="Enter game length (minutes)")
        self.info_lbl.grid(row=0, column=0, columnspan=2, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.time_frm = IntEntry(self, "Time per half", True, 1)
        self.time_frm.grid(row=1, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.half_frm = IntEntry(self, "Half-Time", True, 1)
        self.half_frm.grid(row=1, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.total_lbl = ttk.Label(self, text="Total Game Length: ")
        self.total_lbl.grid(row=2, column=0, columnspan=2, sticky="NSWE",
                            padx=self.pad, pady=self.pad)
        



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Setup")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    setup = SetupFrame(root)
    setup.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()
