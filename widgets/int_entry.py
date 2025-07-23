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

        self.validate_cmd = (self.register(self.validate), '%P')
        self.ent = ttk.Entry(self, textvariable=self.var, validate="key",
                             validatecommand=self.validate_cmd)
        self.ent.grid(row=1, column=0, sticky="NSWE")

    def validate(self, value: str) -> bool:
        '''Validate if the input is an integer within range.
        Register and use as validatecommand in Entry widget
        Returns true if empty or is an integer, otherwise false'''
        #if value == "":
        #    return True
        if not value.isdigit():
            messagebox.showerror("Number Error",
                f"{self.text} must be an integer")
            return False
        elif int(value) < self.min or int(value) > self.max:
            if self.min != minsize and self.max != maxsize:
                messagebox.showerror("Number Error",
                    f"{self.text} must be between {self.min} and {self.max}")
            elif self.max == maxsize:
                messagebox.showerror("Number Error",
                    f"{self.text} must be {self.min} or above")
            else:
                messagebox.showerror("Number Error",
                    f"{self.text} must be {self.max} or below")
            return False
        else:
            return True