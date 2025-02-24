import os
import sys
import pygame
from pydub import AudioSegment


class SoundPlayer:
    # def __init__(self):
    #     self._sound_route = ''

    # @property
    # def sound_route(self):
    #     return self._sound_route     All this shit is commented because its pretty broke

    # @sound_route.setter
    # def sound_route(self, route):
    #     if not route:
    #         raise ValueError("Sound route cannot be empty")
    #     if not os.path.exists(route):
    #         raise FileNotFoundError(f"Sound file not found: {route}")
    #     self._sound_route = route

    def playsound(self, sound_route):
        # if not self._sound_route:
        #     raise ValueError("No sound route set")
            
        try:
            pygame.mixer.init()

            if sound_route == '':
                if sys.platform == "win32":
                    # Windows 10/11 default alarm location
                    sound_path = os.path.join(os.environ['WINDIR'], 'Media', 'Alarm01.wav')

                    # Check if file exists
                    if os.path.exists(sound_path):
                        # Load and play the sound
                        sound = pygame.mixer.Sound(sound_path)
                        sound.play()
                        
                        # Keep program running until sound finishes
                        pygame.time.wait(int(sound.get_length() * 1000))
                    else:
                        print("Default alarm sound not found.")
                    
            else:
                current_route = sound_route
                to_wav = current_route.replace('.webm', '.wav')
                
                if not os.path.exists(to_wav):
                    audio = AudioSegment.from_file(sound_route, format='webm')
                    audio.export(to_wav, format='wav')

                pygame.mixer.init()
                sound = pygame.mixer.Sound(to_wav)
                sound.play()

                while pygame.mixer.get_busy():
                    pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Error in playsound: {e}")
        finally:
            pygame.mixer.quit()