## Spotify playlist
For this project, I am using BeautifulSoup to scrape Billboards top 100 songs from a particular date that the user inputs in the format YYYY-MM-DD. Then I will extract the song titles and use the spotify API to add those songs to a playlist.

Spotify uses OAuth to allow 3rd party apps to access an account. I am using Spotipy, a python module for Spotify to make this easier. 
https://spotipy.readthedocs.io
