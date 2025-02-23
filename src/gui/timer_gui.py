import tkinter as tk
from tkinter import ttk


class TimerComponent(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.timer_widgets()

    def timer_widgets(self):
        self.left_frame = ttk.Frame(self)
        self.right_frame = ttk.Frame(self)
        
        # Place the main frames
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky='n')
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky='n')
        
        # Left section - Time and Start button
        self.label = ttk.Label(self.left_frame, text='Timer')
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        time_frame = ttk.Frame(self.left_frame)
        time_frame.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        self.hour_spinbox = ttk.Spinbox(time_frame, from_=0, to=23, width=6)
        self.hour_spinbox.grid(row=0, column=0, padx=2)
        
        ttk.Label(time_frame, text=":").grid(row=0, column=1, padx=2)
        
        self.minute_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, width=6)
        self.minute_spinbox.grid(row=0, column=2, padx=2)
        
        ttk.Label(time_frame, text=":").grid(row=0, column=3, padx=2)

        self.seconds_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, width=6)
        self.seconds_spinbox.grid(row=0, column=4, padx=2)
        
        self.start_button = ttk.Button(self.left_frame, text="Start")
        self.start_button.grid(row=2, column=0, columnspan=3, pady=(0, 10))

        # Right section - Just sound selection
        sound_frame = ttk.Frame(self.right_frame)
        sound_frame.grid(row=8, column=0, pady=(20, 0))
        
        self.select_sound = ttk.Button(sound_frame, text="Select Sound")
        self.select_sound.grid(row=0, column=0, pady=(0, 5))
        
        self.alarm_sound_selected = ttk.Label(sound_frame, text="Default Sound")
        self.alarm_sound_selected.grid(row=1, column=0)

    def get_timer(self):
        return self.hour_spinbox, self.minute_spinbox, self.seconds_spinbox
