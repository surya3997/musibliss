import pymongo
import eyed3

audio_path = "../../songs/3/Idhazhin Oram.mp3"

audio = eyed3.load(audio_path)

print(audio.tag.artist)
print(audio.tag.album)
print(audio.tag.composer)
print(audio.tag.title)
print(audio.info.time_secs)