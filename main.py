'''Program to run an underwater hockey game.

Opens a setup window to control the game specifications
Runs the game with an input window to control the score,
and an output window to view the scores and times

v1 - Uses setup info to run input and output
v2 - Saves game results after the game

Created by Luke Marshall
08/08/25'''

import tkinter as tk
from setup import SetupFrame
from input import InputFrame
from output import OutputFrame

class Main(tk.Tk):
    '''Runs the underwater hockey game.'''

    def __init__(self):
        super().__init__()

        self.title("Setup")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.geometry("+0+0")

        self.frame = SetupFrame(self)
        self.frame.grid(row=0, column=0, sticky="NSWE")

        self.mainloop()

    def to_input(self, outputs: dict) -> None:
        '''Close setup frame and open input frame and output window.'''
        self.frame.destroy()
        self.frame = InputFrame(self, "results.json", **outputs)
        self.frame.grid(row=0, column=0, sticky="NSWE")
        self.title("Input")

        self.output_win = tk.Toplevel(self)
        self.output_win.title("Output")
        self.output_win.rowconfigure(0, weight=1)
        self.output_win.columnconfigure(0, weight=1)
        self.output_win.geometry("+0+350")
        self.output = OutputFrame(self.output_win, self.frame,
                                  self.frame.w_team, self.frame.b_team,
                                  self.frame.game)
        self.output.grid(row=0, column=0, sticky="NSWE")

Main()
