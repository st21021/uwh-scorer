'''A frame or window to setup an Underwater Hockey game.

v1 - Gets the time for the game and then starts it
v1.1 - Displays total game length correctly
v2 - Gets overtime procedure
v3 - Gets team name abbreviations

Created by Luke Marshall
15/08/25'''

import tkinter as tk
from tkinter import ttk
from custom_style import CustomStyle
from int_entry import IntEntry
from radio_buttons import RadioButtons
from str_entry import StrEntry

class SetupFrame(ttk.Frame):
    '''Frame to setup the underwater hockey game.
    Collects various inputs from the user, e.g. time, teams'''

    def __init__(self, master: tk.Tk | ttk.Frame) -> None:
        '''Create setup frame.'''
        super().__init__(master) # Inherit methods from ttk.Frame

        self.style = CustomStyle(self)
        self.rowconfigure(list(range(8)), weight=1)
        self.columnconfigure(list(range(2)), weight=1)
        self.pad = 10 # Padding between widgets

        self.info_lbl = ttk.Label(self, text="Enter game length (minutes)",
                                  anchor="w")
        self.info_lbl.grid(row=0, column=0, columnspan=2, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.inputs = {} # dict to be able to loop through all inputs

        # Length of each half of the game
        self.inputs["time"] = IntEntry(self, "Time per half", True, 1)
        self.inputs["time"].grid(row=1, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)

        # Length of half-time
        self.inputs["half"] = IntEntry(self, "Half-Time", True, 1)
        self.inputs["half"].grid(row=1, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)

        # Selects the overtime procedure
        self.inputs["overtime"] = RadioButtons(self, "Overtime procedure", [
            "No Overtime",
            "Extra Time",
            "Golden Goal"
        ], 0)
        self.inputs["overtime"].grid(row=2, column=0, rowspan=2, sticky="NSWE",
                         padx=self.pad, pady=self.pad)

        # Length of the extra time halves
        self.inputs["OT_time"] = IntEntry(self, "Extra time per half", False, 1)
        self.inputs["OT_time"].grid(row=2, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        self.inputs["OT_time"].disable() # Disabled until extra time option is selected

        # Length of the break between 2nd half and overtime, and between overtime halves
        self.inputs["OT_break"] = IntEntry(self, "Extra break", False, 1)
        self.inputs["OT_break"].grid(row=3, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        self.inputs["OT_break"].disable() # Disabled until extra time option is selected

        # Total game length
        self.total_lbl = ttk.Label(self, text="Total Game Length: N/A",
                                   anchor="w")
        self.total_lbl.grid(row=4, column=0, columnspan=2, sticky="NSWE",
                            padx=self.pad, pady=self.pad)

        # Team names
        self.name_lbl = ttk.Label(self, text="Enter team name abbreviations",
                                  anchor="w")
        self.name_lbl.grid(row=5, column=0, columnspan=2, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        self.inputs["w_team"] = StrEntry(self, "White Team", False)
        self.inputs["w_team"].grid(row=6, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        self.inputs["b_team"] = StrEntry(self, "Black Team", False)
        self.inputs["b_team"].grid(row=6, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)

        # Starts the game
        self.start_btn = ttk.Button(self, text="Start Game", command=self.start)
        self.start_btn.grid(row=7, column=0, sticky="NSWE",
                            padx=self.pad, pady=self.pad)


    def update(self) -> None:
        '''Update the total game length label.'''

        # Make inputs not required so error messages aren't given
        self.inputs["time"].required = False
        self.inputs["half"].required = False
        time = self.inputs["time"].get()
        half = self.inputs["half"].get()
        self.inputs["time"].required = True
        self.inputs["half"].required = True
        if time != "" and half != "":
            # Calculate total
            total = 2*time + half
            self.total_lbl.configure(text=f"Total Game Length: {total} min")
        else:
            # Not all inputs are given yet
            self.total_lbl.configure(text=f"Total Game Length: N/A")

        # Make inputs not required so error messages aren't given
        self.inputs["OT_time"].required = False
        self.inputs["OT_break"].required = False

        # Check if the Extra Time option has been selected
        if self.inputs["overtime"].get() == "Extra Time":
            # Enable the overtime length inputs
            self.inputs["OT_time"].enable()
            self.inputs["OT_break"].enable()

            ot_time = self.inputs["OT_time"].get()
            ot_break = self.inputs["OT_break"].get()
            if ot_time != "" and ot_break != "" and "total" in locals():
                # If number inputs are all entered and total has been calcuated,
                # Add a worst case scenario time
                ot_total = total + 2*ot_time + 2*ot_break
                self.total_lbl.configure(text=f"Total Game Length: {total}-{ot_total} min")
        else:
            # Disable the overtime length inputs
            self.inputs["OT_time"].disable()
            self.inputs["OT_break"].disable()

    def start(self) -> None:
        '''Start the underwater hockey game.
        Creates the input and output frames'''
        outputs = {}
        valid = True
        if self.inputs["overtime"].get() == "Extra Time":
            self.inputs["OT_time"].required = True
            self.inputs["OT_break"].required = True
        for key, value in self.inputs.items():
            # If .get() returns None, the value is invalid
            if value.get() == None:
                valid = False
            elif value.get() != "":
                # Don't add to outputs if blank, so default values can be used
                outputs[key] = value.get()
        if hasattr(self.master, "to_input"):
            # Will run if the setup frame was created by main
            # Only main has the to_input method
            if valid:
                self.master.to_input(outputs)
        else:
            # Otherwise print results
            if valid:
                print(outputs)
            else:
                print("Invalid")
        return None


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Setup")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = SetupFrame(root)
    frame.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()
