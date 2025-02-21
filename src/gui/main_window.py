import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alarm')
        self.geometry('400x300')

        self.create_widgets()

    def create_widgets(self):
        #Creates a menu item
        self.alarm_menu = tk.Menu(self)
        self.config(menu=self.alarm_menu)
        self.alarm_menu.add_command(label="Alarm")
        self.alarm_menu.add_command(label="Timer")
        self.alarm_menu.add_command(label="Download")



if __name__ == '__main__':
    main_window = MainWindow()
    main_window.mainloop()