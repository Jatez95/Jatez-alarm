import tkinter as tk
from tkinter import ttk
from downloader.yt_downloader import YTDLSource
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

class DownloadComponent(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.download_widget()

    def download_widget(self):
        download_frame = ttk.Frame(self)
        download_frame.grid(row=0, column=0, padx=20, pady=20)
        
        download_frame.grid_columnconfigure(0, weight=1)

        self.label = ttk.Label(download_frame, text='Download Sound')
        self.label.grid(row=0, column=0, pady=(0, 10), sticky='ew')

        entry_frame = ttk.Frame(download_frame)
        entry_frame.grid(row=1, column=0, pady=(0, 10), sticky='ew')
        
        entry_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(entry_frame, text="URL:").grid(row=0, column=0, padx=(0, 5))
        self.url_input = ttk.Entry(entry_frame)
        self.url_input.grid(row=0, column=1, sticky='ew')

        self.download_button = ttk.Button(download_frame, text="Download", command=self.handle_download)
        self.download_button.grid(row=2, column=0, pady=(10, 0), sticky='ew')
    
    def get_entry_url(self):
        return self.url_input.get()

    def download_task(self):
        url_input = self.get_entry_url()
        try:
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            loop.run_until_complete(YTDLSource.from_url(url_input))
            
            self.after(0, lambda: self.label.config(text="Download complete"))
        except Exception as e:
            
            self.after(0, lambda: self.label.config(text=f"Error: {str(e)}"))
        finally:
            
            self.after(0, lambda: self.download_button.config(state='normal'))
            loop.close()

    def handle_download(self):
        
        self.download_button.config(state='disabled')
        self.label.config(text="Downloading...")
        
        thread = threading.Thread(target=self.download_task, daemon=True)
        thread.start()