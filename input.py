'''A frame or window to control an underwater hockey game.

v1 - Runs the game with 2 halves and 1 half-time, with scoring

Created by Luke Marshall
25/07/25'''

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
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
        self.pad = 5 # Padding between widgets
        self.ipad = 10 # Padding inside widgets
        self.bd = 1 # Border width of widgets

        self.time = 10
        self.half = 2
        self.start_time = datetime.now()

        # time_frm contains Time Left, half, and actual time labels
        self.time_frm = ttk.Frame(self, style="box.TFrame")
        self.time_frm.rowconfigure(list(range(2)), weight=1)
        self.time_frm.rowconfigure(2, weight=2)
        self.time_frm.columnconfigure(0, weight=1)
        self.time_frm.grid(row=0, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)

        self.time_left_lbl = ttk.Label(self.time_frm, text="Time Left",
                                       style="med.box.TLabel")
        self.time_left_lbl.grid(row=0, column=0, sticky="NSWE",
                                padx=self.bd, pady=self.bd,
                                ipadx=self.ipad, ipady=self.ipad)

        self.half = tk.StringVar(self, "First Half")
        self.half_lbl = ttk.Label(self.time_frm, textvariable=self.half,
                                  style="box.TLabel")
        self.half_lbl.grid(row=1, column=0, sticky="NSWE",
                           padx=self.bd, pady=self.bd,
                           ipadx=self.ipad, ipady=self.ipad)

        self.time_var = tk.StringVar(self, "10:00")        
        self.time_lbl = ttk.Label(self.time_frm, textvariable=self.time_var,
                                  style="lrg.box.TLabel")
        self.time_lbl.grid(row=2, column=0, sticky="NSWE",
                           padx=self.bd, pady=self.bd,
                           ipadx=self.ipad, ipady=self.ipad)

        self.real_var = tk.StringVar(self, "")        
        self.real_time_lbl = ttk.Label(self, textvariable=self.real_var,
                                  style="box.TLabel")
        self.real_time_lbl.grid(row=2, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        self.update()

    def update(self) -> None:
        '''Updates the time of the window'''
        self.now = datetime.now()
        self.real_var.set(self.now.strftime("%H:%M:%S"))

        diff = self.now - self.start_time
        diff -= timedelta(microseconds=diff.microseconds) # Remove microsecond accuracy
        minutes, seconds = divmod(diff.seconds, 60)
    
        if minutes < self.time:
            diff = timedelta(minutes=self.time) - diff
            minutes, seconds = divmod(diff.seconds, 60)
            self.time_var.set(f"{minutes:02}:{seconds:02}")

        self.after(1000, self.update)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Input")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = InputFrame(root)
    frame.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()