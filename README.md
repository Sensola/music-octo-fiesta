# music-octo-fiesta
Webapp and backend to change music playing in host machine 
uses vlc.py and youtube-dl. There might be some other needed third party libraries.
Currently developing no-javascript version.
##Currently working:
- App can find songs from youtube, parse usefull information and display it.
- When clicked on search results App plays local test song. 
- Pause button stops song from playing.
- Streaming to named pipe works in linux but playing from there does not.
##Todo:
- Make playing from stream work
- Update frontend
- Automated playlist playing favouring users with less songs played recently
- User and Admin pages so that Users can add songs to playlists and Admins can do more advanced stuff
- Add database to store played songs and other usefull data.
