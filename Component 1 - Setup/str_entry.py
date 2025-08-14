import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StrEntry(ttk.Frame):
    '''Frame to get string entry.'''

    def __init__(self, master: tk.Tk | ttk.Frame, text: str,
                 required: bool = False) -> None:
        '''Create frame.'''
        super().__init__(master)

        # Create attributes
        self.text = text
        self.required = required

        self.rowconfigure(list(range(2)), weight=1)
        self.columnconfigure(0, weight=1)

        # Create tkinter/ttk widgets
        self.lbl = ttk.Label(self, text=self.text)
        self.lbl.grid(row=0, column=0)

        self.var = tk.StringVar(self, "")

        self.ent = ttk.Entry(self, textvariable=self.var)
        self.ent.grid(row=1, column=0, sticky="NSWE")
    
    def get(self) -> int | None:
        '''Return the integer from var, or None if invalid.'''
        if self.var.get() == "" and self.required:
            messagebox.showerror("Input Error",
                f"{self.text} cannot be blank")
            return None
        else:
            return self.var.get()
    
    def set(self, value) -> None:
        '''Set the value of var to value.'''
        self.var.set(value)
        return None
    
    def reset(self) -> None:
        '''Empty the entry.'''
        self.var.set("")
        return None
