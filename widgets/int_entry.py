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

        # Create attributes
        self.text = text
        self.required = required
        self.min = min
        self.max = max

        self.rowconfigure(list(range(2)), weight=1)
        self.columnconfigure(0, weight=1)

        # Create tkinter/ttk widgets
        self.lbl = ttk.Label(self, text=self.text)
        self.lbl.grid(row=0, column=0)

        self.var = tk.StringVar(self, "")

        self.validate_cmd = (self.register(self.validate), '%P') # This validates the entries input
        self.ent = ttk.Entry(self, textvariable=self.var, validate="key",
                             validatecommand=self.validate_cmd)
        self.ent.grid(row=1, column=0, sticky="NSWE")

        if hasattr(self.master, "update"):
            self.master.master.bind("<Key>", lambda event: self.master.update())

    def validate(self, value: str) -> bool:
        '''Validate if the input is an integer within range.
        Register and use as validatecommand in Entry widget
        Returns true if empty or is an integer, otherwise false'''
        if value == "" or value == "-":
            return True
        try: # Will raise ValueError if value is not an integer
            if int(value) < self.min or int(value) > self.max:
                # Show an error if value is out of range
                if self.min != minsize and self.max != maxsize:
                    messagebox.showerror("Number Error",
                        f"{self.text} must be between {self.min} and {self.max}")
                
                # Change error message if default min or max is used
                elif self.max == maxsize:
                    messagebox.showerror("Number Error",
                        f"{self.text} must be {self.min} or above")
                else:
                    messagebox.showerror("Number Error",
                        f"{self.text} must be {self.max} or below")
                return False
            else:
                return True
        except ValueError:
            messagebox.showerror("Number Error",
                f"{self.text} must be an integer")
            return False
    
    def get(self) -> int | None:
        '''Return the integer from var, or None if invalid.'''
        try:
            return int(self.var.get())
        except ValueError:
            if self.var.get() == "" and self.required:
                messagebox.showerror("Number Error",
                    f"{self.text} cannot be blank")
                return None
            elif self.var.get() == "":
                # Return blank string if not required
                return ""
            else:
                messagebox.showerror("Number Error",
                    f"'{self.var.get()}' is an invalid value for {self.text}")
                return None
    
    def set(self, value) -> None:
        '''Set the value of var to value.'''
        self.var.set(value)
        return None
    
    def reset(self, value) -> None:
        '''Empty the entry.'''
        self.var.set("")
        return None
