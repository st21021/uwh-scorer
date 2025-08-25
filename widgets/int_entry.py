import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sys import maxsize
minsize = -maxsize - 1


class IntEntry(ttk.Frame):
    """Frame to get integer entry."""

    def __init__(self, master: tk.Tk | ttk.Frame, text: str,
                 required: bool = False,
                 min: int = minsize, max: int = maxsize) -> None:
        """Create frame."""
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

        # This validates the entries input
        self.validate_cmd = (self.register(self.validate), '%P')
        self.ent = ttk.Entry(self, textvariable=self.var, validate="key",
                             validatecommand=self.validate_cmd)
        self.ent.grid(row=1, column=0, sticky="NSWE")

        if hasattr(self.master, "update"):
            self.master.master.bind("<Key>",
                                    lambda event: self.master.update())

    def validate(self, value: str) -> bool:
        """Validate if the input is an integer within range.
        Register and use as validatecommand in Entry widget
        Returns true if empty or is an integer, otherwise false"""
        if value == "" or value == "-":
            return True
        try:  # Will raise ValueError if value is not an integer
            if int(value) < self.min or int(value) > self.max:
                # Show an error if value is out of range
                if self.min != minsize and self.max != maxsize:
                    m = f"{self.text} must be between {self.min} and {self.max}"
                    messagebox.showerror("Number Error", m)

                # Change error message if default min or max is used
                elif self.max == maxsize:
                    m = f"{self.text} must be {self.min} or above"
                    messagebox.showerror("Number Error", m)

                else:
                    m = f"{self.text} must be {self.max} or below"
                    messagebox.showerror("Number Error", m)
                return False
            else:
                return True
        except ValueError:
            m = f"{self.text} must be an integer"
            messagebox.showerror("Number Error", m)
            return False

    def get(self) -> int | None:
        """Return the integer from var, or None if invalid."""
        try:
            return int(self.var.get())
        except ValueError:
            if self.var.get() == "" and self.required:
                m = f"{self.text} cannot be blank"
                messagebox.showerror("Number Error", m)
                return None
            elif self.var.get() == "":
                # Return blank string if not required
                return ""
            else:
                m = f"'{self.var.get()}' is an invalid value for {self.text}"
                messagebox.showerror("Number Error", m)
                return None

    def set(self, value) -> None:
        """Set the value of var to value."""
        self.var.set(value)
        return None

    def reset(self) -> None:
        """Empty the entry."""
        self.var.set("")
        return None

    def disable(self) -> None:
        """Disables input from the entry."""
        self.ent.configure(state="disabled")
        self.lbl.configure(style="disabled.TLabel")
        return None

    def enable(self) -> None:
        """Reenables input from the entry."""
        self.ent.configure(state="normal")
        self.lbl.configure(style="TLabel")
        return None
