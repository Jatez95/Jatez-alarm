from downloader.yt_downloader import YTDLSource
import os
import pathlib
from ctypes import windll
import string
from alarm.alarm_setup import SetupAlarm
from alarm.sound_player import SoundPlayer


class SetOptions:
    def __init__(self):
        self.option = None
        self.userpath = self.obtain_user_path()
        self.set_alarm = SetupAlarm()
        self.sound_player = SoundPlayer()
        self.sound_route = ''

    async def run(self):
        """
        The function that runs the program
        print a menu with options
        
        """
        self.options()
        self.sound_route = "C:/Users/xxjav/Music/alarm-sounds/DESPERTADOR_MR_JAGGER.webm" # Default sound
        self.option = int(input("Introduce your option: "))
        while self.option != 6:
            print(self.sound_route)
            if self.option == 1:
                ytdl_source = YTDLSource()
                await ytdl_source.from_url(self.userpath)
            
            elif self.option == 2:
                self.check_sounds_by_extension()
            
            elif self.option == 3:
                self.set_alarm.alarm_option(self.sound_route)
            elif self.option == 4:
                self.set_alarm.timer_option(self.sound_route)
            elif self.option == 5:
                print(self.sound_route)
                self.select_alarm_sound()
            self.options()
            self.option = int(input("Enter the an option: ")) 

    def options(self):
        print("""
            1.Download Sound
            2.Show all sounds
            3.Setup an alarm
            4.Setup a timer
            5.Set sound
            6.exit
        """)
    
    def select_alarm_sound(self):
        onlyfiles = []
        count = 1
        try:
            # Add error handling for directory access
            sound_directory = f"{self.userpath}/Music/alarm-sounds"
            if not os.path.exists(sound_directory):
                raise FileNotFoundError(f"Directory not found: {sound_directory}")

            for file_sound in os.listdir(sound_directory):
                print(f"{count}. {file_sound}")
                onlyfiles.append(file_sound)
                count += 1
            
            if not onlyfiles:
                raise FileNotFoundError("No sound files found in the directory")

            sound_option = int(input("Introduce the sound you want to reproduce as your alarm: "))
            if sound_option < 1 or sound_option > len(onlyfiles):
                raise ValueError("Invalid sound option selected")

            sound_selected = onlyfiles[sound_option - 1]
            full_path = os.path.join(self.userpath, "Music", "alarm-sounds", sound_selected)
            
            # Use the setter instead of directly accessing the private variable
            self.sound_route = full_path
            print(f"You selected: {sound_selected}")
            print(f"Full path: {full_path}")  # Debug print

        except Exception as e:
            print(f"Error in select_alarm_sound: {e}")
    
    def check_sounds_by_extension(self):
        """
        Check for the audio files and print the ones with (.wav or mp3) extension
        this extensions only works with pygame
        """
        onlyfiles = []
        for f in os.listdir(f"{self.userpath}/Music/alarm-sounds"):
            if pathlib.Path(f).suffix in (".wav", ".mp3"):
                onlyfiles.append(f)
        print(onlyfiles)