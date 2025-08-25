"""A frame or window to view to score/time of an underwater hockey game.

v1 - Displays the time left, stage, real time, team names and scores

Created by Luke Marshall
05/08/25
"""

import tkinter as tk
from tkinter import ttk
from custom_style import CustomStyle


class OutputFrame(ttk.Frame):
    """Frame to view the underwater hockey game.

    Displays the time left and score of the game
    """

    def __init__(self, master: tk.Tk | ttk.Frame, input_frame,
                 w_team: str = "WHITE TEAM", b_team: str = "BLACK TEAM",
                 game: int = 1) -> None:
        """Create input frame."""
        super().__init__(master)  # Inherit methods from ttk.Frame

        self.input = input_frame
        self.style = CustomStyle(self)
        self.rowconfigure(list(range(2)), weight=1)
        self.columnconfigure(list(range(3)), weight=1)
        self.pad = 5  # Padding between widgets
        self.ipad = 10  # Padding inside widgets
        self.bd = 1  # Border width of widgets

        self.w_team = w_team
        self.b_team = b_team
        self.game = game

        # time_frm contains Time Left, stage, and actual time left labels
        self.time_frm = ttk.Frame(self, style="box.TFrame")
        self.time_frm.rowconfigure(list(range(2)), weight=1)
        self.time_frm.rowconfigure(2, weight=2)
        self.time_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.time_frm, 0, 1)

        self.time_left_lbl = ttk.Label(self.time_frm, text="Time Left",
                                       style="med.box.TLabel")
        self.box_grid(self.time_left_lbl, 0, 0, "xy")

        self.stage_lbl = ttk.Label(self.time_frm,
                                   textvariable=self.input.stage_var,
                                   style="box.TLabel")
        self.box_grid(self.stage_lbl, 1, 0, "x")

        self.time_lbl = ttk.Label(self.time_frm,
                                  textvariable=self.input.time_var,
                                  style="lrg.box.TLabel")
        self.box_grid(self.time_lbl, 2, 0, "xy")

        # white_frm contains White, Name and score labels
        self.white_frm = ttk.Frame(self, style="box.TFrame")
        self.white_frm.rowconfigure(list(range(2)), weight=1)
        self.white_frm.rowconfigure(2, weight=2)
        self.white_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.white_frm, 0, 0)

        self.white_lbl = ttk.Label(self.white_frm, text="White",
                                   style="med.white.box.TLabel")
        self.box_grid(self.white_lbl, 0, 0, "xy")

        self.w_team_lbl = ttk.Label(self.white_frm, text=self.w_team,
                                    style="white.box.TLabel")
        self.box_grid(self.w_team_lbl, 1, 0, "x")

        self.w_score_lbl = ttk.Label(self.white_frm,
                                     textvariable=self.input.w_score,
                                     style="lrg.white.box.TLabel")
        self.box_grid(self.w_score_lbl, 2, 0, "xy")

        # black_frm contains Black, Name and score labels
        self.black_frm = ttk.Frame(self, style="box.TFrame")
        self.black_frm.rowconfigure(list(range(2)), weight=1)
        self.black_frm.rowconfigure(2, weight=2)
        self.black_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.black_frm, 0, 2)

        self.black_lbl = ttk.Label(self.black_frm, text="Black",
                                   style="med.black.box.TLabel")
        self.box_grid(self.black_lbl, 0, 0, "xy")

        self.b_team_lbl = ttk.Label(self.black_frm, text=self.b_team,
                                    style="black.box.TLabel")
        self.box_grid(self.b_team_lbl, 1, 0, "x")

        self.b_score_lbl = ttk.Label(self.black_frm,
                                     textvariable=self.input.b_score,
                                     style="lrg.box.TLabel")
        self.box_grid(self.b_score_lbl, 2, 0, "xy")

        # Displays the actual time of day
        self.real_frm = ttk.Frame(self, style="box.TFrame")
        self.real_frm.rowconfigure(0, weight=1)
        self.real_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.real_frm, 2, 0)
        self.real_time_lbl = ttk.Label(self.real_frm,
                                       textvariable=self.input.real_var,
                                       style="box.TLabel")
        self.box_grid(self.real_time_lbl, 0, 0, "xy")

        # Displays the game number, used in a tournament setting
        self.num_frm = ttk.Frame(self, style="box.TFrame")
        self.num_frm.rowconfigure(0, weight=1)
        self.num_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.num_frm, 2, 2)
        self.num_lbl = ttk.Label(self.num_frm, textvariable=self.input.num_var,
                                 style="box.TLabel")
        self.box_grid(self.num_lbl, 0, 0, "xy")

        self.update()

    def frame_grid(self, widget: ttk.Frame, row: int, column: int) -> None:
        """Add a frame into the grid."""
        widget.grid(row=row, column=column, sticky="NSWE",
                    padx=self.pad, pady=self.pad)
        return None

    def box_grid(self, widget: tk.Widget, row: int, col: int,
                 bd: str = "n") -> None:
        """Add a widget into it's frame with a border.

        bd: Use 'x' for left/right, 'y' for top/bottom, 'xy' for both
        """
        widget.grid(row=row, column=col, sticky="NSWE",
                    padx=0, pady=0, ipadx=self.ipad, ipady=self.ipad)
        if "x" in bd.lower():
            widget.grid_configure(padx=self.bd)
        if "y" in bd.lower():
            widget.grid_configure(pady=self.bd)
        return None


if __name__ == "__main__":
    pass
