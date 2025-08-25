import tkinter as tk
from tkinter import ttk


class CustomStyle(ttk.Style):
    '''A Style object that customizes the style of ttk widgets.'''

    def __init__(self, master: tk.Tk | tk.Frame | ttk.Frame) -> None:
        '''Create custom style instance.'''
        super().__init__(master)

        self.bg = "#dddddd"  # Background colour
        self.fg = "#000000"  # Normal text colour

        self.default_box_bg = "#ffffff"  # Background of boxes
        self.default_box_fg = "#000000"  # Text colour in boxes

        self.white_bg = "#ffffff"  # Background for white team
        self.white_fg = "#000000"  # Text colour for white team

        self.black_bg = "#000000"  # Background for black team
        self.black_fg = "#ffffff"  # Text colour for black team

        self.disabled_fg = "#666666"

        self.bd = "#000000"  # Border colour

        self.font = ("Arial", 12)
        self.med_font = ("Arial", 24)
        self.lrg_font = ("Arial", 36)

        # Button press colours
        self.bg_active = "#bbbbbb"
        self.fg_active = "#000000"
        self.w_bg_active = "#888888"
        self.w_fg_active = "#ffffff"
        self.b_bg_active = "#888888"
        self.b_fg_active = "#000000"

        self.theme_use('alt')

        self.config()

    def config(self) -> None:
        '''Configure the style options.'''
        self.configure("TFrame", background=self.bg)
        self.configure("box.TFrame", background=self.bd)

        self.configure("TLabel", background=self.bg, foreground=self.fg,
                       font=self.font, anchor="center")
        self.configure("disabled.TLabel", foreground=self.disabled_fg)
        self.configure("box.TLabel", background=self.default_box_bg,
                       foreground=self.default_box_fg)
        self.configure("white.box.TLabel", background=self.white_bg,
                       foreground=self.white_fg)
        self.configure("black.box.TLabel", background=self.black_bg,
                       foreground=self.black_fg)

        self.configure("med.box.TLabel", font=self.med_font)
        self.configure("lrg.box.TLabel", font=self.lrg_font)
        self.configure("med.white.box.TLabel", font=self.med_font)
        self.configure("lrg.white.box.TLabel", font=self.lrg_font)
        self.configure("med.black.box.TLabel", font=self.med_font)
        self.configure("lrg.black.box.TLabel", font=self.lrg_font)

        self.configure("TButton", background=self.bg, foreground=self.fg,
                       font=self.font, anchor="center")
        self.configure("white.TButton", background=self.white_bg,
                       foreground=self.white_fg)
        self.configure("black.TButton", background=self.black_bg,
                       foreground=self.black_fg)
        self.map(
            "TButton",
            background=[
                ("active", self.bg_active)
            ],
            foreground=[
                ("active", self.fg_active)
            ]
        )
        self.map(
            "white.TButton",
            background=[
                ("active", self.w_bg_active)
            ],
            foreground=[
                ("active", self.w_fg_active)
            ]
        )
        self.map(
            "black.TButton",
            background=[
                ("active", self.b_bg_active)
            ],
            foreground=[
                ("active", self.b_fg_active)
            ]
        )

        self.configure("TRadiobutton", background=self.bg, foreground=self.fg,
                       font=self.font)
        self.map(
            "TRadiobutton",
            background=[
                ("active", self.bg_active)
            ],
            foreground=[
                ("active", self.fg_active)
            ],
            indicatorcolor=[
                ("pressed", self.bg_active),
                ("selected", self.bg_active)
            ]
        )
        return None
