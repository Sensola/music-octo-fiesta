import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import json


def find(source, song):
    if source == "YouTube":
        return youtube(song)


def youtube(song):
    # data = ""
    data = []
    search = song
    query = urllib.parse.quote(search)
    url = "https://www.youtube.com/results?search_query="+query
    r = urllib.request.urlopen(url)
    html = r.read()
    soup = BeautifulSoup(html, "html.parser")
    i = 0;
    for vid in soup.findAll(attrs={"class": "yt-uix-tile-link"}):


        vidurl = "https://www.youtube.com"+vid["href"]

        dataquery = urllib.parse.quote(vidurl)
        dataurl = "https://www.youtube.com/oembed?url={}&format=json".format(dataquery)

        # todo: Moms spaghetti, find error and fix it
        try:
            datar = urllib.request.urlopen(dataurl)
        except:
            continue

        datahtml = datar.read()
        datasoup = BeautifulSoup(datahtml, "html.parser")

        jsonpaska = json.loads(datasoup.decode("utf-8", "replace"))

        # Take only thumbnail, title and authorname from json
        turnip = {}

        if "author_name" not in jsonpaska:
            continue

        for key in ("thumbnail_url","title","author_name"):
            turnip[key] = jsonpaska[key]
        turnip["vidurl"] = vidurl
        data.append(turnip)
        # data = data + "<li><div class='search_result'><div class='thumbnail'><img src={} height='100px'></div><div class='song_info'><p>{}</p><br><p>{}</p></div><br><br></div></li>".format(jsonpaska["thumbnail_url"],jsonpaska["title"],jsonpaska["author_name"])

        i+=1
        if i >= 5:   #TODO: option to show more
            break
    return data


def spotify(song):
    pass


def soundcloud(song):
    pass
