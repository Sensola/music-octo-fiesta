import os
import subprocess
# import vlc
import time
source = "https://www.youtube.com/watch?v=bd2B6SjMh_w"
source2 = "https://www.youtube.com/watch?v=E4yjpT8dkLw"

PIPENAME = "piipe"

def start_streaming(source):
    VLC = "\"C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe\""
    ytdl = "youtube-dl -o - "
    stream_process = os.popen("youtube-dl -o - {} > {} ".format(source, PIPENAME))
    return stream_process

def play():
    time.sleep(4)
    #os.system("cat < " + PIPENAME)
    print("mui")
    #p = vlc.MediaPlayer('fd://{}'.format(PIPENAME))
    ## p.play()


class VLCController:
    VLC = "\"C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe\""

    def play_new(self, source):
        print("streaming")
        # todo: use subprocess and make vlc controllable
        ytdl = "youtube-dl -o - {}".format(source)
        youtube_dl = subprocess.Popen(ytdl, stdout=subprocess.PIPE)
        os.system("youtube-dl -o - {} | {} - ".format(source,  self.VLC))
        os.system("{} vlc://quit".format(self.VLC))

    def pause(self):
        pass

def main2():
    vlc = VLCController()
    playlist = [source,source2]
    while playlist:
        vlc.play_new(playlist.pop(0))
def main():
    a = start_streaming(source)
    play()
    input("Close")
    a.close()

if __name__ == "__main__":
    main()
# import subprocess

# proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
# (out, err) = proc.communicate()
# print "program output:", out

