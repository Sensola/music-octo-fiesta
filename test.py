from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import mecha
import player

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.query_string:
        source = request.args.get("source")
        song = request.args.get("song")
        data = mecha.find(source, song)

    if request.method == "POST":
        video = request.form["song"]
        player.play_song(video)

    return render_template("Index2.html",
                           style = url_for("static", filename="style.css"),
                           velho = url_for("static", filename="velho.jpg"),
                           data = data)


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