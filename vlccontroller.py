import os
#  import subprocess
import vlc
import time
source = "https://www.youtube.com/watch?v=bd2B6SjMh_w"
source2 = "https://www.youtube.com/watch?v=E4yjpT8dkLw"

PIPENAME = "piipe"


b = 1
def play():

    time.sleep(4)
    # os.system("cat < " + PIPENAME)
    print("mui")
    p = vlc.MediaPlayer("Gnarls Barkley - Crazy-bd2B6SjMh_w.webm")  # 'fd://{}'.format(PIPENAME))
    input()

    b = 1

    p.play()
    c = {"p": p.pause,
         "s": p.stop,
         "y": p.play
        }
    while 1:
        afg = input("give command")
        if afg in c:
            c[afg]()
        else:
            print("p: pause/unpause", "s: stop", "y: play")


class PlayerController:
    """Class to handle playlists, control VLC player using vlc.py and stream videos using youtube-dl"""
    # todo: rename
    PIPENAME = "piipe"
    YTDL = "youtube-dl -o - "
    stream_process = None

    def __init__(self, playlist=[].copy(), player=None):
        self.playlist = playlist
        if not player:
            self.player = vlc.MediaPlayer()

    def append(self, link):
        # todo: Make work with users so that after f.ex. three songs playlist prefers users with fever songs on list
        self.playlist.append(link)

    def stream_to_pipe(self, source):
        """:param source: link to start streaming with youtube-dl"""
        if self.stream_process:
            self.stream_process.stop()
        self.stream_process = os.popen("youtube-dl -o - {} > {} ".format(source, PIPENAME))

    def play_next(self):
        # todo: test and
        link = self.playlist.pop[0]
        self.stream_to_pipe(link)
        #instance = vlc.Instance()
        #media = instance.media_new("fd://"+self.PIPENAME)
        #self.player.set_media(media)
        self.player.play()

    def override_play_local(self,song):

        instance = vlc.Instance()
        media = instance.media_new(song)
        self.player.set_media(media)

    def override_play_song(self, song):
        instance = vlc.Instance()
        media = instance.media_new("test.webm")
        self.player.set_media(media)
        self.player.play()

    def override_stop(self):
        self.player.stop()

    def override_quit_player(self):
        self.__exit__()

    def pause(self):
        self.player.pause()

    def __enter__(self):
        pass

    def __exit__(self):
        if self.stream_process:
            self.stream_process.close()
        if self.player:
            self.player.stop()
        del self.player
        self.player = None


def main():
    with PlayerController() as player:
        player.play()

if __name__ == "__main__":
    main()


