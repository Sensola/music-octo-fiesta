from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import mecha
#import player
import vlccontroller
app = Flask(__name__)

player = vlccontroller.PlayerController()
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
            player.append(video)
            player.override_play_song(video)
            data = None
        elif "pause" in request.form:
            player.override_quit_player()
        else:
            error = "Not yet implemented"
    return render_template("Index3.html",
                           style = url_for("static", filename="style.css"),
                           velho = url_for("static", filename="velho.jpg"),
                           data = data,
                           error = error)


@app.route("/place/")
def place():
    return "Place"


@app.route("/holder/")
def holder():
    return "Holder"


@app.route("/lyrics/")
def lyrics():
    return "Lyrics page"

if __name__ == "__main__":
    app.debug = True
    app.run()