import tkinter as tk
from tkinter import ttk


class RadioButtons(ttk.Frame):
    """Frame to get multiple choice input."""

    def __init__(self, master: tk.Tk | ttk.Frame, text: str, values: list,
                 default_index: int = False) -> None:
        """Create frame."""
        super().__init__(master)

        # Create attributes
        self.text = text
        self.values = values
        self.rowconfigure(list(range(len(values)+1)), weight=1)
        self.columnconfigure(0, weight=1)

        # Create tkinter/ttk widgets
        self.lbl = ttk.Label(self, text=self.text)
        self.lbl.grid(row=0, column=0)

        self.var = tk.StringVar(self, "")
        if (isinstance(default_index, int) and
                not isinstance(default_index, bool)):
            # Set var to default value if index is given
            self.var.set(self.values[default_index])

        buttons = []
        for value in values:
            buttons.append(ttk.Radiobutton(self, text=value, value=value,
                                           variable=self.var))
            buttons[-1].grid(row=values.index(value)+1, column=0,
                             sticky="NSWE")
            if hasattr(self.master, "update"):
                buttons[-1].configure(command=self.master.update)

    def get(self) -> str | None:
        """Return the str from var"""
        return self.var.get()

    def set(self, value) -> None:
        """Set the value of var to value."""
        self.var.set(value)
        return None
