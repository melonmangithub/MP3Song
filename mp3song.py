import youtubesearchpython
import webbrowser
import os
import time

# pip install youtubesearchpython
# use: MP3Song("name", "artist").play()

class MP3Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.loaded = False
        
        query = self.name + self.artist + "offical audio"
        videos = youtubesearchpython.VideosSearch(query, limit = 1)
        self.link = videos.result()["result"][0]["link"]
        
        self.loaded = True
        
    def play(self):
        if self.loaded:
            webbrowser.open(self.link)