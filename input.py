'''A frame or window to control an underwater hockey game.

v1 - Runs the game with 2 halves and 1 half-time, with scoring

Created by Luke Marshall
25/07/25'''

import tkinter as tk
from tkinter import ttk
from custom_style import CustomStyle

class InputFrame(ttk.Frame):
    '''Frame to run the underwater hockey game.
    Displays the time left, and buttons to control the score/time'''

    def __init__(self, master: tk.Tk | ttk.Frame) -> None:
        '''Create input frame.'''
        super().__init__(master) # Inherit methods from ttk.Frame

        self.style = CustomStyle(self)
        self.rowconfigure(list(range(3)), weight=1)
        self.columnconfigure(list(range(3)), weight=1)
        self.pad = 5

        # time_frm contains Time Left, half, and actual time labels
        self.time_frm = ttk.Frame(self)
        self.time_frm.rowconfigure(list(range(2)), weight=1)
        self.time_frm.rowconfigure(2, weight=2)
        self.time_frm.columnconfigure(0, weight=1)
        self.time_frm.grid(row=0, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)

        self.time_left_lbl = ttk.Label(self.time_frm, text="Time Left")
        self.time_left_lbl.grid(row=0, column=0, sticky="NSWE",
                                padx=self.pad, pady=self.pad)
        
        self.half = tk.StringVar(self, "First Half")
        self.half_lbl = ttk.Label(self.time_frm, textvariable=self.half)
        self.half_lbl.grid(row=1, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)

        self.time_var = tk.StringVar(self, "10:00")        
        self.time_lbl = ttk.Label(self.time_frm, textvariable=self.time_var)
        self.time_lbl.grid(row=2, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Input")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = InputFrame(root)
    frame.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()