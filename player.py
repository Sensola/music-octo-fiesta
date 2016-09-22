import pafy


def play_song(song):
    url = song
    video = pafy.new(url)
    streams = video.streams
    bestaudio = video.getbestaudio()


    print("\n")
    print(video.title)
    print(bestaudio.bitrate, bestaudio.get_filesize())
    print("\n")
    print(bestaudio.url)
    print("\n")
