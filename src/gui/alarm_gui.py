import tkinter as tk
from tkinter import ttk

class AlarmComponent(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.var_monday = tk.IntVar(value=0)
        self.var_tuesday = tk.IntVar(value=0)
        self.var_wednesday = tk.IntVar(value=0)
        self.var_thursday = tk.IntVar(value=0)
        self.var_friday = tk.IntVar(value=0)
        self.var_saturday = tk.IntVar(value=0)
        self.var_sunday = tk.IntVar(value=0)
        self.create_widgets()

    def create_widgets(self):
        # Create main frames for left and right sections
        self.left_frame = ttk.Frame(self)
        self.right_frame = ttk.Frame(self)
        
        # Place the main frames
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky='n')
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky='n')
        
        # Left section - Time and Start button
        self.label = ttk.Label(self.left_frame, text='Alarm')
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Time spinboxes in a horizontal layout
        time_frame = ttk.Frame(self.left_frame)
        time_frame.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        self.hour_spinbox = ttk.Spinbox(time_frame, from_=0, to=23, width=6)
        self.hour_spinbox.grid(row=0, column=0, padx=2)
        
        ttk.Label(time_frame, text=":").grid(row=0, column=1, padx=2)
        
        self.minute_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, width=6)
        self.minute_spinbox.grid(row=0, column=2, padx=2)
        
        self.start_button = ttk.Button(self.left_frame, text="Start")
        self.start_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        
        # Right section - Days and Sound
        days_label = ttk.Label(self.right_frame, text='Select Days')
        days_label.grid(row=0, column=0, pady=(0, 10))
        
        # Days checkboxes
        self.checkbox_monday = ttk.Checkbutton(self.right_frame, text="Monday", variable=self.var_monday)
        self.checkbox_monday.grid(row=1, column=0, sticky='w')
        
        self.checkbox_tuesday = ttk.Checkbutton(self.right_frame, text="Tuesday", variable=self.var_tuesday)
        self.checkbox_tuesday.grid(row=2, column=0, sticky='w')
        
        self.checkbox_wednesday = ttk.Checkbutton(self.right_frame, text="Wednesday", variable=self.var_wednesday)
        self.checkbox_wednesday.grid(row=3, column=0, sticky='w')
        
        self.checkbox_thursday = ttk.Checkbutton(self.right_frame, text="Thursday", variable=self.var_thursday)
        self.checkbox_thursday.grid(row=4, column=0, sticky='w')
        
        self.checkbox_friday = ttk.Checkbutton(self.right_frame, text="Friday", variable=self.var_friday)
        self.checkbox_friday.grid(row=5, column=0, sticky='w')
        
        self.checkbox_saturday = ttk.Checkbutton(self.right_frame, text="Saturday", variable=self.var_saturday)
        self.checkbox_saturday.grid(row=6, column=0, sticky='w')
        
        self.checkbox_sunday = ttk.Checkbutton(self.right_frame, text="Sunday", variable=self.var_sunday)
        self.checkbox_sunday.grid(row=7, column=0, sticky='w')
        
        # Sound selection
        sound_frame = ttk.Frame(self.right_frame)
        sound_frame.grid(row=8, column=0, pady=(20, 0))
        
        self.select_sound = ttk.Button(sound_frame, text="Select Sound")
        self.select_sound.grid(row=0, column=0, pady=(0, 5))
        
        self.alarm_sound_selected = ttk.Label(sound_frame, text="Default Sound")
        self.alarm_sound_selected.grid(row=1, column=0)

    def get_alarm_time(self):
        return self.hour_spinbox.get(), self.minute_spinbox.get()

    def get_days(self):
        return {
            'monday': self.var_monday.get(),
            'tuesday': self.var_tuesday.get(),
            'wednesday': self.var_wednesday.get(),
            'thursday': self.var_thursday.get(),
            'friday': self.var_friday.get(),
            'saturday': self.var_saturday.get(),
            'sunday': self.var_sunday.get()
        }
    
    def get_selected_days(self):
        return [day for day, value in self.get_days().items() if value == 1]
    

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
    

class DownloadComponent(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.download_widget()

    def download_widget(self):
        download_frame = ttk.Frame(self)
        download_frame.grid(row=0, column=0, padx=20, pady=20)
        
        # Configure column weights for download_frame
        download_frame.grid_columnconfigure(0, weight=1)

        self.label = ttk.Label(download_frame, text='Download Sound')
        self.label.grid(row=0, column=0, pady=(0, 10), sticky='ew')

        # Entry frame setup
        entry_frame = ttk.Frame(download_frame)
        entry_frame.grid(row=1, column=0, pady=(0, 10), sticky='ew')
        
        # Configure column weights for entry_frame
        entry_frame.grid_columnconfigure(1, weight=1)

        # URL label and entry
        ttk.Label(entry_frame, text="URL:").grid(row=0, column=0, padx=(0, 5))
        self.url_input = ttk.Entry(entry_frame)
        self.url_input.grid(row=0, column=1, sticky='ew')

        # Download button
        self.download_button = ttk.Button(download_frame, text="Download")
        self.download_button.grid(row=2, column=0, pady=(10, 0), sticky='ew')