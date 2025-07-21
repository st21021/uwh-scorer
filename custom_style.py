import tkinter as tk
from tkinter import ttk

class CustomStyle(ttk.Style):
    '''A Style object that customizes the style of ttk widgets.'''

    def __init__(self, master: tk.Tk | tk.Frame | ttk.Frame) -> None:
        '''Create custom style instance.'''
        super().__init__(master)

        self.bg = "#dddddd"
        self.fg = "#000000"
        self.font = ("Arial", 12)
        self.accent1 = "#000088"
        self.accent2 = "#0000ff"

        self.config()
    
    def config(self) -> None:
        '''Configure the style options.'''
        self.configure("TFrame", background=self.bg)

        self.configure("TLabel", background=self.bg, foreground=self.fg,
                       font=self.font, anchor="center")
        
        self.configure("TButton", background=self.bg, foreground=self.fg,
                       font=self.font, anchor="center")
        self.map(
            "TButton",
            background=[
                ("active", self.accent1),
                ("pressed", self.accent2)
            ],
            foreground=[
                ("active", self.fg),
                ("pressed", self.accent2)
            ]
        )