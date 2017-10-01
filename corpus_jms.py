from PyLyrics import *

fo = open("corpus_jms.txt", "w")
albums = PyLyrics.getAlbums(singer='Juan Gabriel')
for myalbum in albums:
    tracks = myalbum.tracks()
    for track in tracks:
        try:
            print("Here")
            #print (track) #Each track is a track object
            fo.write(track.getLyrics()) #Get the lyrics
        except:
            continue
fo.close()
