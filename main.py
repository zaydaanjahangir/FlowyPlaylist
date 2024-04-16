import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME']  = 'Spotify Cookie'

with open("app_secret.txt", "r") as secret_file: # store app secret in a separate txt file
        app_secret = secret_file.read().strip()
app.secret_key = app_secret

TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('create_flowy_playlist', external = True))

@app.route('/createFlowyPlaylist')
def create_flowy_playlist():
    try:
        token_info = get_token()
    except:
        print("User not logger in")
        return redirect("/")
    
    sp = spotipy.Spotify(auth = token_info['access_token'])
    user_id = sp.current_user()['id']

    current_playlists = sp.current_user_playlists()['items']
    test_playlist_id = None

    print("Current playlists:") #debugging
    for playlist in current_playlists:
        print(playlist['name'])

    for playlist in current_playlists:  # Searches for input playlist named "Test"
        if(playlist['name'] == 'Test'):
            test_playlist_id = playlist['id']
        
    if not test_playlist_id: 
        return "Test playlist was not found"
    
     # Get features for each song in the "Test" playlist
    test_playlist = sp.playlist_items(test_playlist_id)
    song_features = []
    for song in test_playlist['items']:
        track_id = song['track']['id']
        features = sp.audio_features(track_id)
        if features:
            song_features.append(features[0])
    
    
def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external=False))
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth(): #add your own clientid and secret in a separate file
    with open("client_id.txt", "r") as id_file: 
        client_id = id_file.read().strip() 

    with open("secret.txt", "r") as secret_file:
        client_secret = secret_file.read().strip()

    return SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=url_for('redirect_page', _external=True),
        scope='user-library-read playlist-modify-public playlist-modify-private playlist-read-private audio-features'
    )


app.run(debug=True)