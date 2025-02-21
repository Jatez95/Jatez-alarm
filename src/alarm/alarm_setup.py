import datetime
import time
from .sound_player import SoundPlayer


class SetupAlarm:
    def __init__(self):
        """
        The class attributtes
        """

        self.init_time = datetime.datetime.now() # Current time this will be the start time and this is updated
        self.given_time = '' # The time the alarm will start playing
        self.init_seconds = 0 #The conversion of the start time to seconds
        self.end_seconds = 0 #The conversion of the end time to seconds
        self.sound_player = SoundPlayer
        

    def ask_for_time(self):
        """
        Ask for the time the sound will start playing
        
        no args needed
        """
        try:
            self.given_time = input('Enter the time the alarm will start playing (H:M): ')
            self.given_time = datetime.datetime.strptime(self.given_time, '%H:%M')
            self.check_time()
        except ValueError as ve:
            print(f'Error: {ve}')
            self.ask_for_time()
    
    def check_time(self):
        """
        Check if the given time have a correct format
        then with a loop checks if the start time is greater than the end time
        if is greater ask for the time again
        
        no args needed
        """
        if datetime.datetime.strftime(self.init_time, '%H:%M') and datetime.datetime.strftime(self.given_time, '%H:%M'):
            print('Time is correct')
            self.init_seconds = self.init_time.hour * 3600 + self.init_time.minute * 60
            self.end_seconds = self.given_time.hour * 3600 + self.given_time.minute * 60
            
            while self.init_seconds > self.end_seconds: # check if the start time is greater than the end time
                print('The format was correct but the start time is greater than the end time')
                print(f'The {self.given_time.hour}:{self.given_time.minute} is less than {self.init_time.hour}:{self.init_time.minute}')
                self.ask_for_time()
                self.init_seconds = self.init_time.hour * 3600 + self.init_time.minute * 60
                self.end_seconds = self.given_time.hour * 3600 + self.given_time.minute * 60
            
            
        
        else:
            self.given_time = input('Enter the time you want to end the alarm must be (H:M): ')
            self.given_time = datetime.datetime.strptime(self.given_time, '%H:%M')
            self.check_time()
    
    def alarm_option(self, sound_route):
        """
        Run the alarm clock checking everytime if the current time is equal to the end time
        if the two times are equal the sound will start playing

        no args needed
        """
        self.ask_for_time()
        print(f"the alarm will sound at {self.given_time.hour:02}:{self.given_time.minute:02}")

        while self.init_seconds != self.end_seconds and not self.init_seconds > self.end_seconds:
            self.init_time = datetime.datetime.now()
            self.init_seconds = self.init_time.hour * 3600 + self.init_time.minute * 60
            print(f"Current time: {self.init_time.hour:02}:{self.init_time.minute:02}:{self.init_time.second:02}")
            time.sleep(1)
            

        if self.init_seconds == self.end_seconds:
            self.sound_player.playsound(sound_route)
            
    
    def timer_option(self, sound_route):

        """
        Run the timer checking everytime if the current time is equal to the end time
        if the two times are equal the sound will start playing
        """
        
        self.given_time = input('Enter the your timer (H:M:S): ')
        self.given_time = datetime.datetime.strptime(self.given_time, '%H:%M:%S')
        print(self.given_time)
        if datetime.datetime.strftime(self.given_time, '%H:%M:%S'):
            self.end_seconds = self.given_time.hour * 3600 + self.given_time.minute * 60 + self.given_time.second
        else:
            print("You must enter the time with this format: (H:M:S)")
            self.timer_option(sound_route)
        
        
        
        for counting_seconds in range(self.end_seconds, 0, -1):
            seconds = counting_seconds % 60
            minutes = int(counting_seconds / 60) % 60
            hours = int(counting_seconds / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            if counting_seconds == 1:
                self.sound_player.playsound(sound_route)
            time.sleep(1) 