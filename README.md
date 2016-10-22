# music-octo-fiesta
Webapp and backend to change music playing in host machine 
Streaming from youtube is made with youtube-dl and the stream is piped straight to vlc. Idea is to use vlc.py to controll vlc but there is some problems playing from named pipe so it isn't implemented yet.  Webapp backend is made with flask.

Currently developing no-javascript version.

##Currently working:
- App can find songs from youtube, parse usefull information and display it.
- When clicked on search results App plays clicked song
- Streaming to named pipe works in linux but there is issues with vlc to play from it.

##Todo:
- Make playing from stream work
- Update frontend
- Automated playlist playing favouring users with less songs played recently
- User and Admin pages so that Users can add songs to playlists and Admins can do more advanced stuff
- Add database to store played songs and other usefull data.
