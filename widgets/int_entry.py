import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sys import maxsize
minsize = -maxsize - 1

class IntEntry(ttk.Frame):
    '''Frame to get integer entry.'''

    def __init__(self, master: tk.Tk | ttk.Frame, text: str,
                 required: bool = False,
                 min: int = minsize, max: int = maxsize) -> None:
        '''Create frame.'''
        super().__init__(master)

        self.text = text
        self.required = required
        self.min = min
        self.max = max

        self.rowconfigure(list(range(2)), weight=1)
        self.columnconfigure(0, weight=1)

        self.lbl = ttk.Label(self, text=self.text)
        self.lbl.grid(row=0, column=0)

        self.var = tk.IntVar(self, "")

        self.ent = ttk.Entry(self, textvariable=self.var)
        self.ent.grid(row=1, column=0, sticky="NSWE")
