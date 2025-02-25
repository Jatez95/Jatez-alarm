import tkinter as tk
from tkinter import ttk, filedialog
import datetime
from downloader.yt_downloader import YTDLSource
from alarm.sound_player import SoundPlayer

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
        self.setted_alarm = tk.IntVar()
        self.sound_file_route = ''
        self.sound_player = SoundPlayer()
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
        
        self.start_button = ttk.Button(self.left_frame, text="Start", command=self.check_time)
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
        
        self.select_sound_button = ttk.Button(sound_frame, text="Select Sound", command=self.select_sound)
        self.select_sound_button.grid(row=0, column=0, pady=(0, 5))
        
        self.alarm_sound_selected = ttk.Label(sound_frame, text="Default Sound")
        self.alarm_sound_selected.grid(row=1, column=0)
    
    def select_sound(self):
        user_route = YTDLSource().obtain_user_path()
        self.sound_file_route = filedialog.askopenfilename(
            filetypes=(("wav files", "*.wav"), ("mp3 files", "*,mp3"), ("all files", "*.*")), 
            initialdir=f"{user_route}/Music/alarm-sounds"
        )

        sound_file = self.sound_file_route.split("/", -1)

        sound_file = sound_file[-1]

        self.alarm_sound_selected.config(text=sound_file.replace("_", " "))
        print(self.sound_file_route)

    def get_alarm_time(self):
        time = f"{self.hour_spinbox.get()}:{self.minute_spinbox.get()}"
        to_datetime = datetime.datetime.strptime(time, "%H:%M")
        return to_datetime

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
    
    
    def start_alarm(self):
        
        # Get alarm time
        alarm_time = self.get_alarm_time()
        
        # Get selected days
        days = self.get_selected_days()
        day_names = ", ".join(days) if days else "every day"
        
        
        # Start checking
        self.check_time()
    
    def check_time(self):
        now = datetime.datetime.now()
        alarm_time =self.get_alarm_time()
        
        # Check if current time matches alarm time
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            # Check if today is a selected day, or if no days are selected (meaning all days)
            selected_days = self.get_selected_days()
            weekday = now.strftime("%A").lower()
            
            if not selected_days or weekday in selected_days:
                for x in range(0, 3):
                    self.sound_player.playsound(self.sound_file_route)
        
        else:
            # Schedule next check (every second)
            self.alarm_check_id = self.after(1000, self.check_time)
            