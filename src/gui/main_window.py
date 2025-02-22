import tkinter as tk
from gui.alarm_gui import AlarmComponent, TimerComponent, DownloadComponent

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alarm')
        self.geometry('400x300')

        self.create_widgets()

    def create_widgets(self):
        self.create_menu()

        self.alarm_component = AlarmComponent(self)
        self.alarm_component.pack(padx=20, pady=20)

    def widget_timer(self):
        self.create_menu()

        self.alarm_component = TimerComponent(self)
        self.alarm_component.pack(padx=20, pady=20)

    def widget_download(self):
        self.create_menu()

        self.alarm_component = DownloadComponent(self)
        self.alarm_component.pack(padx=20, pady=20)
        
        
    
    def create_menu(self):
        #Creates a menu item
        self.alarm_menu = tk.Menu(self)
        self.config(menu=self.alarm_menu)
        self.alarm_menu.add_command(label="Alarm", command=self.create_widgets)
        self.alarm_menu.add_command(label="Timer", command=self.widget_timer)
        self.alarm_menu.add_command(label="Download", command = self.widget_download)