import tkinter as tk
from tkinter import ttk

class CustomStyle(ttk.Style):
    ''''''

    def __init__(self, master: tk.Tk | tk.Frame | ttk.Frame) -> None:
        super().__init__(self, master)
