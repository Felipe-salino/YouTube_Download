from pytubefix import *

yt = YouTube(input('Coloque aqui a URl:'))

print(yt.title)

print(yt.thumbnail_url)

stream = yt.streams.get_highest_resolution()

stream.download()
