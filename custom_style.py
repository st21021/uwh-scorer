import tkinter as tk
from tkinter import ttk

class CustomStyle(ttk.Style):
    '''A Style object that customizes the style of ttk widgets'''

    def __init__(self, master: tk.Tk | tk.Frame | ttk.Frame) -> None:
        '''Create custom style instance'''
        super().__init__(master)

        self.configure("TLabel", background="#dddddd", foreground="#000000",
                       font=("Arial", 10, "bold"), anchor="center")