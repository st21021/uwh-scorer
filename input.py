'''A frame or window to control an underwater hockey game.

v1 - Runs the game with 2 halves and 1 half-time, with scoring

Created by Luke Marshall
31/07/25'''

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

        self.time = 10 # Length of each half of the game
        self.half = 2 # Length of half-time
        self.start_time = datetime.now()

        self.w_team = "HOW SO"
        self.b_team = "GDC SO"
        self.game = 20

        # time_frm contains Time Left, stage, and actual time left labels
        self.time_frm = ttk.Frame(self, style="box.TFrame")
        self.time_frm.rowconfigure(list(range(2)), weight=1)
        self.time_frm.rowconfigure(2, weight=2)
        self.time_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.time_frm, 0, 1)

        self.time_left_lbl = ttk.Label(self.time_frm, text="Time Left",
                                       style="med.box.TLabel")
        self.widget_grid(self.time_left_lbl, 0, 0, "xy")

        self.stage_var = tk.StringVar(self, "First Half")
        self.stage_lbl = ttk.Label(self.time_frm, textvariable=self.stage_var,
                                  style="box.TLabel")
        self.widget_grid(self.stage_lbl, 1, 0, "x") 

        self.time_var = tk.StringVar(self, "10:00")        
        self.time_lbl = ttk.Label(self.time_frm, textvariable=self.time_var,
                                  style="lrg.box.TLabel")
        self.widget_grid(self.time_lbl, 2, 0, "xy")
        
        # white_frm contains White, Name and score labels
        self.white_frm = ttk.Frame(self, style="box.TFrame")
        self.white_frm.rowconfigure(list(range(2)), weight=1)
        self.white_frm.rowconfigure(2, weight=2)
        self.white_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.white_frm, 0, 0)

        self.white_lbl = ttk.Label(self.white_frm, text="White",
                                   style="med.white.box.TLabel")
        self.widget_grid(self.white_lbl, 0, 0, "xy") 

        self.w_team_lbl = ttk.Label(self.white_frm, text=self.w_team,
                                    style="white.box.TLabel")
        self.widget_grid(self.w_team_lbl, 1, 0, "x")

        self.w_score = tk.IntVar(self, 0)        
        self.w_score_lbl = ttk.Label(self.white_frm, textvariable=self.w_score,
                                     style="lrg.white.box.TLabel")
        self.widget_grid(self.w_score_lbl, 2, 0, "xy")

        # black_frm contains Black, Name and score labels
        self.black_frm = ttk.Frame(self, style="box.TFrame")
        self.black_frm.rowconfigure(list(range(2)), weight=1)
        self.black_frm.rowconfigure(2, weight=2)
        self.black_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.black_frm, 0, 2)

        self.black_lbl = ttk.Label(self.black_frm, text="Black",
                                   style="med.black.box.TLabel")
        self.widget_grid(self.black_lbl, 0, 0, "xy")

        self.b_team_lbl = ttk.Label(self.black_frm, text=self.b_team,
                                    style="black.box.TLabel")
        self.widget_grid(self.b_team_lbl, 1, 0, "x")

        self.b_score = tk.IntVar(self, 0)        
        self.b_score_lbl = ttk.Label(self.black_frm, textvariable=self.b_score,
                                     style="lrg.box.TLabel")
        self.widget_grid(self.b_score_lbl, 2, 0, "xy")

        # Displays the actual time of day
        self.real_frm = ttk.Frame(self, style="box.TFrame")
        self.real_frm.rowconfigure(0, weight=1)
        self.real_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.real_frm, 2, 0)
        self.real_var = tk.StringVar(self, "")        
        self.real_time_lbl = ttk.Label(self.real_frm,
                                       textvariable=self.real_var,
                                       style="box.TLabel")
        self.widget_grid(self.real_time_lbl, 0, 0, "xy")

        # Displays the game number, used in a tournament setting
        self.num_frm = ttk.Frame(self, style="box.TFrame")
        self.num_frm.rowconfigure(0, weight=1)
        self.num_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.num_frm, 2, 2)
        self.num_var = tk.StringVar(self, f"Game no. {self.game}")        
        self.num_lbl = ttk.Label(self.num_frm, textvariable=self.num_var,
                                 style="box.TLabel")
        self.widget_grid(self.num_lbl, 0, 0, "xy")

        self.update()

    def update(self) -> None:
        '''Updates the time of the window.'''
        self.now = datetime.now()
        self.real_var.set(self.now.strftime("%H:%M:%S"))

        diff = self.now - self.start_time
        diff -= timedelta(microseconds=diff.microseconds) # Remove microsecond accuracy
        seconds = diff.seconds

        # In first half
        if seconds < self.time:
            self.change_time(diff, lambda: self.time)

        # Start of half-time
        elif seconds == self.time:
            self.change_stage("Half-Time", "Break")
            self.change_time(diff, lambda: self.time + self.half)

        # In half-time
        elif seconds < self.time + self.half:
            self.change_time(diff, lambda: self.time + self.half)

        # Start of second half
        elif seconds == self.time + self.half:
            self.change_stage("Second Half", "Normal")
            self.change_time(diff, lambda: 2*self.time + self.half)

        # In second half
        elif seconds < 2*self.time + self.half:
            self.change_time(diff, lambda: 2*self.time + self.half)
        
        elif seconds == 2*self.time + self.half:
            self.change_time(diff, lambda: 2*self.time + self.half)

        # Runs update() again in 1 second
        self.after(1000, self.update)

    def change_time(self, diff: timedelta, func) -> None:
        '''Change the time label.'''
        time_left = timedelta(seconds=func()) - diff
        minutes, seconds = divmod(time_left.seconds, 60)
        self.time_var.set(f"{minutes:02}:{seconds:02}")
        return None

    def change_stage(self, stage: str, stage_type: str) -> None:
        '''Change the stage label and background colour.'''
        if stage_type == "Timeout":
            # Change background colour to red, and store actual stage
            self.style.bg = "#ff0000"
            self.style.config()
            self.actual_stage = self.stage_var.get()

        elif stage_type == "Break":
            # Change background colour to yellow
            self.style.bg = "#ffff00"
            self.style.config()
        else:
            # Change background colour to normal
            self.style.bg = "#dddddd"
            self.style.config()
        
        # Change label
        self.stage_var.set(stage)
        return None

    def frame_grid(self, widget: ttk.Frame, row: int, column: int) -> None:
        '''Add a frame into the grid.'''
        widget.grid(row=row, column=column, sticky="NSWE",
                    padx=self.pad, pady=self.pad)
        return None

    def widget_grid(self, widget: tk.Widget, row: int, col: int,
                    bd: str = "n") -> None:
        '''Add a widget into it's frame with a border.

        bd: Use "x" for left/right, "y" for top/bottom, "xy" for both'''
        widget.grid(row=row, column=col, sticky="NSWE",
                    padx=0, pady=0, ipadx=self.ipad, ipady=self.ipad)
        if "x" in bd.lower():
            widget.grid_configure(padx=self.bd)
        if "y" in bd.lower():
            widget.grid_configure(pady=self.bd)
        return None



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Input")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = InputFrame(root)
    frame.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()