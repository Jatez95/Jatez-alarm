import tkinter as tk
from tkinter import ttk, filedialog
import datetime
from alarm.sound_player import SoundPlayer
from downloader.yt_downloader import YTDLSource

class TimerComponent(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.timer_widgets()
        self.sound_player = SoundPlayer()
        self.sound_file_route = ''

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
        
        self.start_button = ttk.Button(self.left_frame, text="Start", command=self.timer_window)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=(0, 10))

        # Right section - Just sound selection
        sound_frame = ttk.Frame(self.right_frame)
        sound_frame.grid(row=8, column=0, pady=(20, 0))
        
        self.select_sound = ttk.Button(sound_frame, text="Select Sound", command=self.select_sound)
        self.select_sound.grid(row=0, column=0, pady=(0, 5))
        
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

        

    def get_timer(self):
        
        time = f"{self.hour_spinbox.get():02}:{self.minute_spinbox.get():02}:{self.seconds_spinbox.get():02}"
        to_datetime = datetime.datetime.strptime(time, "%H:%M:%S")
        return to_datetime
    
    def timer_window(self):
        top_window = tk.Toplevel(self)
        top_window.title("Timer")
        top_window.geometry("300x200")
        timer = self.get_timer()

        self.text_var = tk.StringVar()
        self.text_var.set(f"{timer.hour:02}:{timer.minute:02}:{timer.second:02}")

        self.is_paused = tk.BooleanVar()
        self.is_paused.set(False)

        # Create a main frame to hold all elements
        main_frame = ttk.Frame(top_window)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Pack elements into the centered frame
        self.top_label = ttk.Label(main_frame, textvariable = self.text_var)
        self.top_label.pack(pady=10)
        

        self.stop_button = ttk.Button(main_frame, text="Stop", command=self.pause_timer)
        self.stop_button.pack(pady=5)

        button_close = ttk.Button(main_frame, text="Close", command = lambda:self.close_top_window(top_window))
        button_close.pack(pady=5)

        self.update_timer()

    def update_timer(self):
        
        timer = datetime.datetime.strptime(self.text_var.get(), "%H:%M:%S")


        all_seconds = timer.hour * 3600 +  timer.minute * 60 + timer.second

        if self.is_paused.get() == False:

            if all_seconds == 0:
                self.text_var.set("Time is over")
                self.sound_player.playsound(self.sound_file_route)
            else:
                all_seconds = all_seconds - 1


                seconds = all_seconds % 60
                minutes = int(all_seconds / 60) % 60
                hours = int(all_seconds / 3600)

                timer = datetime.datetime.strptime(f"{str(hours)}:{str(minutes)}:{str(seconds)}", "%H:%M:%S")

                self.text_var.set(f"{timer.hour:02}:{timer.minute:02}:{timer.second:02}")

                self.top_label.config(textvariable = self.text_var)
                self.top_label.after(1000, self.update_timer)
            
    
    def pause_timer(self):
        self.is_paused.set(True)

        self.stop_button.config(text="Continue", command=self.continue_timer)

    def continue_timer(self):
        self.is_paused.set(False)

        self.update_timer()

        self.stop_button.config(text="Stop", command=self.pause_timer)
        

    


    
    def close_top_window(self, top_window):
        top_window.destroy()
