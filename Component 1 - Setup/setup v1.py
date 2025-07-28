'''A frame or window to setup an Underwater Hockey game.

v1 - Gets the time for the game and then starts it

Created by Luke Marshall
25/07/2025'''

import tkinter as tk
from tkinter import ttk
from custom_style import CustomStyle
from int_entry import IntEntry

class SetupFrame(ttk.Frame):
    '''Frame to setup the underwater hockey game.
    Collects various inputs from the user, e.g. time, teams'''

    def __init__(self, master: tk.Tk | ttk.Frame) -> None:
        '''Create setup frame.'''
        super().__init__(master) # Inherit methods from ttk.Frame

        self.style = CustomStyle(self)
        self.rowconfigure(list(range(4)), weight=1)
        self.columnconfigure(list(range(2)), weight=1)
        self.pad = 5 # Padding between widgets

        self.info_lbl = ttk.Label(self, text="Enter game length (minutes)")
        self.info_lbl.grid(row=0, column=0, columnspan=2, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.inputs = {} # dict to be able to loop through all inputs

        self.inputs["time"] = IntEntry(self, "Time per half", True, 1)
        self.inputs["time"].grid(row=1, column=0, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.inputs["half"] = IntEntry(self, "Half-Time", True, 1)
        self.inputs["half"].grid(row=1, column=1, sticky="NSWE",
                           padx=self.pad, pady=self.pad)
        
        self.total_lbl = ttk.Label(self, text="Total Game Length: ")
        self.total_lbl.grid(row=2, column=0, columnspan=2, sticky="NSWE",
                            padx=self.pad, pady=self.pad)
        
        self.start_btn = ttk.Button(self, text="Start Game", command=self.start)
        self.start_btn.grid(row=3, column=0, sticky="NSWE",
                            padx=self.pad, pady=self.pad)

    def start(self) -> None:
        '''Start the underwater hockey game.
        Creates the input and output frames'''
        outputs = {}
        valid = True
        for key, value in self.inputs.items():
            # If .get() returns None, the value is invalid
            if value.get() != None:
                outputs[key] = value.get()
            else:
                valid = False
        if valid:
            print(outputs)
        else:
            print("Invalid")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Setup")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = SetupFrame(root)
    frame.grid(row=0, column=0, sticky="NSWE")

    root.mainloop()
