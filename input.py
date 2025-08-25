"""A frame or window to control an underwater hockey game.

v1 - Runs the game with 2 halves and 1 half-time, with scoring
v2 - Saves the results of the game at the end
v2.1 - Adds confirmation message for goals during half-time
v3 - Overhauled time logic, added overtime procedures for ties

Created by Luke Marshall
21/08/25
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
import json
from custom_style import CustomStyle
from output import OutputFrame


class InputFrame(ttk.Frame):
    """Frame to run the underwater hockey game.

    Displays the time left, and buttons to control the score/time
    """

    def __init__(self, master: tk.Tk | ttk.Frame,
                 save_fp: str = "results.json", time: int = 10,
                 half: int = 2, overtime: str = "No Overtime",
                 ot_time: int = 0, ot_break: int = 0,
                 w_team: str = "WHITE TEAM", b_team: str = "BLACK TEAM",
                 game: int = 1) -> None:
        """Create input frame.

        master: tkinter window or frame to place input frame in
        save_fp: json file path to save game results to
        time: length of each half of the game
        half: length of half-time
        overtime: "No Overtime", "Extra Time" or "Golden Goal"
        ot_time: length of each half of overtime
        ot_break: time between overtime halves
        w_team: abbreviated white team name
        b_team: abbreviated black team name
        game: game number (doesn't matter in this context but useful later)
        """
        super().__init__(master)  # Inherit methods from ttk.Frame

        self.save_fp = save_fp  # Json file path to save the game results to
        self.time = time  # Length of each half of the game
        self.half = half  # Length of half-time
        self.overtime = overtime  # Overtime procedure when game ends in a tie
        self.ot_time = ot_time  # Length of each half of overtime
        self.ot_break = ot_break  # Time between overtime halves
        self.w_team = w_team
        self.b_team = b_team
        self.game = game  # Game number
        self.start_time = datetime.now()
        self.time_to_remove = 0
        self.time_to_get_to = self.time

        self.style = CustomStyle(self)
        self.rowconfigure(list(range(3)), weight=1)
        self.columnconfigure(list(range(3)), weight=1)
        self.pad = 5  # Padding between widgets
        self.ipad = 10  # Padding inside widgets
        self.bd = 1  # Border width of widgets

        # time_frm contains 'Time Left', stage, and actual time left labels
        self.time_frm = ttk.Frame(self, style="box.TFrame")
        self.time_frm.rowconfigure(list(range(2)), weight=1)
        self.time_frm.rowconfigure(2, weight=2)
        self.time_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.time_frm, 0, 1)

        self.time_left_lbl = ttk.Label(self.time_frm, text="Time Left",
                                       style="med.box.TLabel")
        self.box_grid(self.time_left_lbl, 0, 0, "xy")

        self.stage_var = tk.StringVar(self, "First Half")
        self.stage_lbl = ttk.Label(self.time_frm, textvariable=self.stage_var,
                                   style="box.TLabel")
        self.box_grid(self.stage_lbl, 1, 0, "x")

        self.time_var = tk.StringVar(self, "10:00")
        self.time_lbl = ttk.Label(self.time_frm, textvariable=self.time_var,
                                  style="lrg.box.TLabel")
        self.box_grid(self.time_lbl, 2, 0, "xy")

        # white_frm contains 'White', name, and score labels
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

        self.w_score = tk.IntVar(self, 0)
        self.w_score_lbl = ttk.Label(self.white_frm, textvariable=self.w_score,
                                     style="lrg.white.box.TLabel")
        self.box_grid(self.w_score_lbl, 2, 0, "xy")

        # black_frm contains 'Black',name, and score labels
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

        self.b_score = tk.IntVar(self, 0)
        self.b_score_lbl = ttk.Label(self.black_frm, textvariable=self.b_score,
                                     style="lrg.box.TLabel")
        self.box_grid(self.b_score_lbl, 2, 0, "xy")

        # Button to add score to the white team
        self.white_btn = ttk.Button(self, text="White Score +1",
                                    command=lambda: self.add_score("w"),
                                    style="white.TButton")
        self.frame_grid(self.white_btn, 1, 0)
        self.white_btn.grid_configure(ipadx=self.ipad, ipady=self.ipad)

        # Button to add score to the black team
        self.black_btn = ttk.Button(self, text="Black Score +1",
                                    command=lambda: self.add_score("b"),
                                    style="black.TButton")
        self.frame_grid(self.black_btn, 1, 2)
        self.black_btn.grid_configure(ipadx=self.ipad, ipady=self.ipad)

        # Displays the actual time of day
        self.real_frm = ttk.Frame(self, style="box.TFrame")
        self.real_frm.rowconfigure(0, weight=1)
        self.real_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.real_frm, 2, 0)
        self.real_var = tk.StringVar(self, "")
        self.real_time_lbl = ttk.Label(self.real_frm,
                                       textvariable=self.real_var,
                                       style="box.TLabel")
        self.box_grid(self.real_time_lbl, 0, 0, "xy")

        # Displays the game number, used in a tournament setting
        # Doesn't actually matter too much when doing 1 game at a time
        self.num_frm = ttk.Frame(self, style="box.TFrame")
        self.num_frm.rowconfigure(0, weight=1)
        self.num_frm.columnconfigure(0, weight=1)
        self.frame_grid(self.num_frm, 2, 2)
        self.num_var = tk.StringVar(self, f"Game no. {self.game}")
        self.num_lbl = ttk.Label(self.num_frm, textvariable=self.num_var,
                                 style="box.TLabel")
        self.box_grid(self.num_lbl, 0, 0, "xy")

        # Updates the time labels every second
        self.update()

    def update(self) -> None:
        """Updates the time of the window."""
        self.now = datetime.now()
        self.real_var.set(self.now.strftime("%H:%M:%S"))

        # Calc difference between now and start, remove microsecond accuracy
        diff = self.now - self.start_time
        diff -= timedelta(microseconds=diff.microseconds)
        seconds = diff.seconds - self.time_to_remove
        # time_to_remove is the sum of halves/breaks already passed

        if self.stage_var.get() == "Golden Goal":
            # In golden goal, time counts upward from 0:00
            self.change_time(seconds)

        elif seconds < self.time_to_get_to:
            # Set time to difference between end of half/break and now
            # Counts down
            self.change_time(self.time_to_get_to-seconds)

        elif seconds == self.time_to_get_to:
            # When the end of a break/half is reached, change the stage
            match self.stage_var.get():
                case "First Half":
                    self.change_stage("Half-Time", "Break")
                    self.time_to_remove += self.time
                    self.time_to_get_to = self.half
                case "Half-Time":
                    self.change_stage("Second Half", "Normal")
                    self.time_to_remove += self.half
                    self.time_to_get_to = self.time
                case "Second Half":
                    if (self.w_score.get() != self.b_score.get() or
                            self.overtime == "No Overtime"):
                        # If game is not tied, or overtime is not needed
                        self.save()
                        # Inform user game has ended and ask to close
                        if messagebox.askyesno("Game over",
                                               "Game over. Close window?"):
                            self.master.destroy()

                    # Otherwise overtime procedures are used
                    elif self.overtime == "Golden Goal":
                        self.change_stage("Golden Goal", "Timeout")
                        self.time_to_remove += self.time
                        self.time_to_get_to = 0
                    elif self.overtime == "Extra Time":
                        self.change_stage("Extra Time Break", "Timeout")
                        self.time_to_remove += self.time
                        self.time_to_get_to = self.ot_break
                case "Extra Time Break":
                    self.change_stage("Extra Time 1st Half", "Timeout")
                    self.time_to_remove += self.ot_break
                    self.time_to_get_to = self.ot_time
                case "Extra Time 1st Half":
                    self.change_stage("Extra Half-Time", "Timeout")
                    self.time_to_remove += self.ot_time
                    self.time_to_get_to = self.ot_break
                case "Extra Half-Time":
                    self.change_stage("Extra Time 2nd Half", "Timeout")
                    self.time_to_remove += self.ot_break
                    self.time_to_get_to = self.ot_time
                case "Extra Time 2nd Half":
                    if self.w_score.get() != self.b_score.get():
                        # If game is not tied
                        self.save()
                        # Inform user game has ended and ask to close
                        if messagebox.askyesno("Game over",
                                               "Game over. Close window?"):
                            self.master.destroy()
                    else:
                        # If still a tie, go into golden goal
                        self.change_stage("Golden Goal", "Timeout")
                        self.time_to_remove += self.ot_time
                        self.time_to_get_to = 0
            seconds = diff.seconds - self.time_to_remove
            self.change_time(self.time_to_get_to-seconds)

        # Runs update() again in 1 second
        self.update_command = self.after(1000, self.update)
        return None

    def change_time(self, seconds: int) -> None:
        """Change the time label."""
        minutes, seconds = divmod(seconds, 60)
        self.time_var.set(f"{minutes:02}:{seconds:02}")
        return None

    def change_stage(self, stage: str, stage_type: str) -> None:
        """Change the stage label and background colour.

        stage_type: 'Normal', 'Break' or 'Timeout'
        """
        if stage_type == "Timeout":
            # Change background colour to red, and store actual stage
            self.style.bg = "#ff0000"
            self.style.config()
            self.actual_stage = self.stage_var.get()
            # Actual stage will be used by ref/team timeouts

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

    def add_score(self, colour: str) -> None:
        """Add score to one of the teams.

        colour: 'w' or 'b'
        """
        add = True  # Will be set to false if user has made a mistake
        if (self.stage_var.get() == "Half-Time" or
                self.stage_var.get() == "Extra Half-Time" or
                self.stage_var.get() == "Extra Time Break"):
            m = "It is half-time. Add score anyway?"
            add = messagebox.askyesno("Add Score", m)
        elif self.stage_var.get() == "Timeout":
            m = "Game is on a timeout. Add score anyway?"
            add = messagebox.askyesno("Add Score", m)

        if add:
            if colour == "w":
                self.w_score.set(self.w_score.get()+1)
            elif colour == "b":
                self.b_score.set(self.b_score.get()+1)
        if self.stage_var.get() == "Golden Goal":
            # If game was in golden goal, adding score will end the game
            self.save()
            if messagebox.askyesno("Game over",
                                   "Game has ended. Close window?"):
                self.master.destroy()
        return None

    def save(self) -> None:
        """Save the game scores to a json file."""
        self.after_cancel(self.update_command)  # Stops time from updating
        try:
            # Open json file to read
            with open(self.save_fp, "r") as f:
                results = json.load(f)
        except FileNotFoundError:
            # Create json file if not found
            with open(self.save_fp, "x") as f:
                results = {"save_error": []}
        except json.decoder.JSONDecodeError:
            # Create empty dict if json file is empty
            results = {"save_error": []}

        if str(self.game) in results.keys():
            # Add game results to save_error list in dictionary
            m = f"Could not save, results for game no. {self.game} already exists"
            messagebox.showerror("Save Error", m)
            results["save_error"].append({
                "w_team": self.w_team,
                "b_team": self.b_team,
                "w_score": self.w_score.get(),
                "b_score": self.b_score.get(),
                "start_time": self.start_time.strftime("%H:%M:%S")
            })
        else:
            # Otherwise add result to dictionary as normal
            results[self.game] = {
                "w_team": self.w_team,
                "b_team": self.b_team,
                "w_score": self.w_score.get(),
                "b_score": self.b_score.get(),
                "start_time": self.start_time.strftime("%H:%M:%S")
            }

        # Save dictionary to the json file
        with open(self.save_fp, "w") as f:
            json.dump(results, f, indent=4)
        return None


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Input")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = InputFrame(root, "results.json", 10, 2)
    frame.grid(row=0, column=0, sticky="NSWE")

    output_win = tk.Toplevel(root)
    output_win.title("Output")
    output_win.rowconfigure(0, weight=1)
    output_win.columnconfigure(0, weight=1)
    output = OutputFrame(output_win, frame, frame.w_team, frame.b_team,
                         frame.game)
    output.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()
