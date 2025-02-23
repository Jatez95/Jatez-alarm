import tkinter as tk
from gui.alarm_gui import AlarmComponent
from gui.timer_gui import TimerComponent
from gui.download_gui import DownloadComponent
from tkinter import ttk
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alarm')
        self.geometry('400x300')

        self.current_component = None
        self.create_menu()
        self.create_widgets()

    def on_closing(self):
        self.destroy()

    def create_menu(self):
        #Creates a menu item
        self.alarm_menu = tk.Menu(self)
        self.config(menu=self.alarm_menu)
        self.alarm_menu.add_command(label="Alarm", command=self.create_widgets)
        self.alarm_menu.add_command(label="Timer", command=self.widget_timer)
        self.alarm_menu.add_command(label="Download", command = self.widget_download)

    
    def clear_current_component(self):

        if self.current_component is not None:
            self.current_component.destroy()

    def create_widgets(self):
        self.clear_current_component()
        self.current_component = AlarmComponent(self)
        self.current_component.pack(padx=20, pady=20)

    def widget_timer(self):
        self.clear_current_component()

        self.current_component = TimerComponent(self)
        self.current_component.pack(padx=20, pady=20)

    def widget_download(self):
        self.clear_current_component()

        self.current_component = DownloadComponent(self)
        self.current_component.pack(padx=20, pady=20)
        
        
    
    