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

        datar = urllib.request.urlopen(dataurl)
        datahtml = datar.read()
        datasoup = BeautifulSoup(datahtml, "html.parser")

        jsonpaska = json.loads(datasoup.decode("utf-8", "replace"))

        # Take only thumbnail, title and authorname from json
        turnip = {}
        for key in ("thumbnail_url","title","author_name"):
            turnip[key] = jsonpaska[key]
        turnip["vidurl"]=vidurl
        data.append(turnip)

        i += 1
        if i >= 5:  # TODO: option to show more
            break
    return data


def spotify(song):
    pass


def soundcloud(song):
    pass
