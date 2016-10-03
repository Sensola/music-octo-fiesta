import os
import subprocess
import vlc
source = "https://www.youtube.com/watch?v=bd2B6SjMh_w"
source2 = "https://www.youtube.com/watch?v=E4yjpT8dkLw"

def start_streaming(source):
    VLC = "\"C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe\""
    ytdl = "youtube-dl -o - "
    server = "NamedPipeServer.exe"
    pipename = "\"SensosNamedPipe\""
    command = "{} {} | {} {}".format(ytdl,source, server, pipename)
    os.system("youtube-dl -o - {} | {} {} ".format(source, server, pipename))
    #with subprocess.Popen(command) as a:
     #   pass

def play():
    p = vlc.MediaPlayer('fd://SensosNamedPipe')

    p.play()


class VLCController:
    VLC = "\"C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe\""

    def play_new(self, source):
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
    start_streaming(source)
    play()

if __name__ == "__main__":
    main()
# import subprocess

# proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
# (out, err) = proc.communicate()
# print "program output:", out

