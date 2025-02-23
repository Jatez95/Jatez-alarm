import yt_dlp
import asyncio
import yt_dlp.downloader
import os
import pathlib
from ctypes import windll
import string

yt_dlp.utils.bug_reports_message = lambda: ''



ffmpeg_options = {
    'options': '-vn',
}


class YTDLSource():
    def __init__(self, *, volume = 0.5):
            self.volume = volume

    @classmethod
    def obtain_user_path(self):
        """
        Obtain the user drive letter example ('C' or 'D')
        then checks if the Users folder is in it
        Example: if Users folder is in C or D will assign user_route this route: C:/Users/user_name
        this route will be used to see the sounds of the alarm 
        """
        user_route = ''
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives() # Copied from stackoverflow
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1
        
        for letter in drives:
            disk_folder = os.listdir(f"{letter}:/") # My creationçç
            if 'Users' in disk_folder:
                user_route = f"{letter}:/Users/{os.getlogin()}"
            
        if not os.path.isdir(f"{user_route}/Music/alarm-sounds"):
            pathlib.Path(user_route, "Music", "alarm-sounds").mkdir(parents=True, exist_ok=True)

        return user_route


    @classmethod
    async def from_url(self, video_url, loop=None, stream=False, ):
        user_route = self.obtain_user_path()

        ytdl_format_options = {
            'format': 'bestaudio/best',
            'outtmpl': user_route + '/Music/alarm-sounds/%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto',
            'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
        }

        loop = loop or asyncio.get_event_loop()

        with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
            try:
                info = await loop.run_in_executor(
                    None,
                    lambda: ydl.extract_info(video_url, download=not stream)
                ) 
                if 'entries' in info:
                    video = info['entries'][0] # get the first video of a playlist
                else:
                    video = info
            except Exception as e:
                print(f"Downlaod failed {e}")
                raise e 
        

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.from_url()) #dunno if this is used i will leave it here