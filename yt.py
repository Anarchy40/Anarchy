import pytube
from time import sleep
import os
from pyfiglet import Figlet


f = Figlet(font='slant')
print(f.renderText('Y0u+uB3-D7'))

url = input('Enter video url:')
youtube = pytube.YouTube(url)
tits = youtube.title()
print('[+]Getting streams-list for:',tits)
strema = youtube.streams.all()


for i in strema:
    print(i)

x = input('Enter itag id:')
vid = youtube.streams.get_by_itag(x)
#Add path of preference
vid.download('Desktop/Necromoda')

print('done')
os.system('cvlc conv.mp4')
os.close('fd')
