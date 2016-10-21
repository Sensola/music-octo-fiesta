from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import send_from_directory
import subprocess
import mecha
import os
import signal
# import vlccontroller
# player = vlccontroller.PlayerController()
# Todo: Make work with vlcController so that user have more controll on playing song.


class Player:
    VLC = "\"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc\""

    def __init__(self):
        self.stream_process = None

    def stream_to_vlc(self, link):
        if self.stream_process:
            os.killpg(os.getpgid(self.stream_process.pid), signal.SIGTERM)
            self.stream_process.kill()
        self.stream_process = subprocess.Popen("youtube-dl -o - {} | {} - --play-and-exit".format(link, self.VLC),
                                               shell=True,
                                               preexec_fn=os.setsid())

    def override_quit_player(self):
        self.stream_process.kill()
player = Player()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = False
    if request.query_string:
        source = request.args.get("source")
        song = request.args.get("song")
        data = mecha.find(source, song)

    if request.method == "POST":
        if "song" in request.form:
            video = request.form["song"]
            player.stream_to_vlc(video)
            data = None

        elif "pause" in request.form:
            player.override_quit_player()
        else:
            error = "Not yet implemented"
    return render_template("Index3.html",
                           style=url_for("static", filename="style.css"),
                           velho=url_for("static", filename="velho.jpg"),
                           data=data,
                           error=error)


@app.route("/place/")
def place():
    return "Place"


@app.route("/holder/")
def holder():
    return "Holder"


@app.route("/lyrics/")
def lyrics():
    return "Lyrics page"


@app.route("/admin")
def admin():
    pass


@app.route("/asdf")
def asdf():
    return render_template("noscript_test.html", style=url_for("static", filename="asdf.css"))


@app.route('/data_getter/<path:path>')
def get_data(path):
    if path == "play.gif":
        print("####PRESSED PLAY")
    return send_from_directory('data_getter', path)


@app.route("/404",  methods=["GET", "POST"])
def _404():
    # todo: draw current playlist, allow to change order or add songs directly to playlist. Add controls
    return render_template("404.html", style=url_for("static", filename="style.css")), 404

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
