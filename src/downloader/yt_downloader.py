import yt_dlp
import asyncio
import yt_dlp.downloader

yt_dlp.utils.bug_reports_message = lambda: ''



ffmpeg_options = {
    'options': '-vn',
}


class YTDLSource():
    def __init__(self, *, volume = 0.5):
            self.volume = volume
            self.url = ''


    @classmethod
    async def from_url(self, user_path, loop=None, stream=False, ):
        ytdl_format_options = {
            'format': 'bestaudio/best',
            'outtmpl': user_path + '/Music/alarm-sounds/%(title)s.%(ext)s',
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
        self.url = input("Introduce la URL del video: ")

        with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
            info = ydl.extract_info(self.url, download=not stream)
            if 'entries' in info:
                video = info['entries'][0] # get the first video of a playlist
            else:
                video = info 
        

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.from_url()) #dunno if this is used i will leave it here