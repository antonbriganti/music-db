import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "check_file"
SPOTIPY_CLIENT_SECRET = "check_file"
SPOTIPY_REDIRECT_URI = "http://localhost"

def get_album_genre(album_name, artist):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="", client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, username="fake"))
    search_term = artist + " " + album_name
    results = sp.search(search_term, limit=1, type="album")
    
    if len(results["albums"]["items"]) > 0:
        artist_spotify_id = results["albums"]["items"][0]["artists"][0]['id']

        results = sp.artist(artist_spotify_id)
        spotify_genres = results["genres"]

        # print(artist_name, artist_spotify_id, spotify_genres)
        return{'spotify_genres': spotify_genres}
    else:
        print(search_term, "not found")
        return{}


# def get_spotify_genres(db_table):
#     Release = Query()
#     for item in db_table:
#         if "spotify_genres" not in item:
#             genres = spotify_api_caller.get_album_genre(item["Release"], item["Artist"])
#             if len(genres) > 0:
#                 db_table.upsert(genres, Release.Release == item["Release"])
