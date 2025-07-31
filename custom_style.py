import tkinter as tk
from tkinter import ttk

class CustomStyle(ttk.Style):
    '''A Style object that customizes the style of ttk widgets.'''

    def __init__(self, master: tk.Tk | tk.Frame | ttk.Frame) -> None:
        '''Create custom style instance.'''
        super().__init__(master)

        self.bg = "#dddddd" # Background colour
        self.fg = "#000000" # Normal text colour

        self.default_box_bg = "#ffffff" # Background of boxes
        self.default_box_fg = "#000000" # Text colour in boxes
        
        self.white_box_bg = "#ffffff" # Background for white team
        self.white_box_fg = "#000000" # Text colour for white team

        self.black_box_bg = "#000000" # Background for black team
        self.black_box_fg = "#ffffff" # Text colour for black team
        
        self.bd = "#000000" # Border colour

        self.font = ("Arial", 12)
        self.med_font = ("Arial", 24)
        self.lrg_font = ("Arial", 36)

        # Accent colours
        self.accent1 = "#000088"
        self.accent2 = "#0000ff"

        self.config()
    
    def config(self) -> None:
        '''Configure the style options.'''
        self.configure("TFrame", background=self.bg)
        self.configure("box.TFrame", background=self.bd)

        self.configure("TLabel", background=self.bg, foreground=self.fg,
                       font=self.font, anchor="center")
        self.configure("box.TLabel", background=self.default_box_bg,
                       foreground=self.default_box_fg)
        self.configure("white.box.TLabel", background=self.white_box_bg,
                       foreground=self.white_box_fg)
        self.configure("black.box.TLabel", background=self.black_box_bg,
                       foreground=self.black_box_fg)

        self.configure("med.box.TLabel", font=self.med_font)
        self.configure("lrg.box.TLabel", font=self.lrg_font)
        self.configure("med.white.box.TLabel", font=self.med_font)
        self.configure("lrg.white.box.TLabel", font=self.lrg_font)
        self.configure("med.black.box.TLabel", font=self.med_font)
        self.configure("lrg.black.box.TLabel", font=self.lrg_font)


        
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
        return None
