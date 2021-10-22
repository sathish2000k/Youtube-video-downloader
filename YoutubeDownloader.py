from pytube import YouTube
from pytube import Playlist

SAVE_PATH = "C:\Windows\TI"  #your location 

url =input("enter the url:")
print("v for video & p for playlist")
i=input("whether playlist or video")

if i=='v':
    my_video = YouTube(url)
    my_video=my_video.streams.filter(res="480p").first()
    my_video.download(SAVE_PATH)
    print(my_video.title)
else:
    my_playlist = Playlist(url)
    for video in my_playlist.videos:
        print(video.title)
        video.streams.filter(res="480p").first().download(SAVE_PATH)
print("------------------------------------------------------------")