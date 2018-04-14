import os
import eyed3
from pymongo import MongoClient
client  = MongoClient("mongodb://hd15pd38:hd15pd38@localhost:27017/hd15pd38")
db = client.hd15pd38
path = "../../songs/"
x = [(i[0],i[2]) for i in os.walk(path)]
name = []
fullPath = []
noSongs = 0
for t in x:
	for f in t[1]:
		if f[-3:] == 'mp3' or f[-3:] == 'MP3':
			name.append(f)
			fullPath.append(t[0] + '/' + f)

collection = db.songs
for i in fullPath:
	audio = eyed3.load(i)
	collection.insert_one({"song_path" : i,
	"song_title" : audio.tag.title,
	"song_album" : audio.tag.album,
	"song_artist" : audio.tag.artist,
	"song_composer" : audio.tag.composer,
	"song_length" : audio.info.time_secs})

#print(audio.tag.artist)
#print(audio.tag.album)
#print(audio.tag.composer)
#print(audio.tag.title)
#print(audio.info.time_secs)

