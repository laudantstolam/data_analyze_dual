# import necessary modules
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect, jsonify,  render_template
import pandas as pd
import requests
import json

# initialize Flask app
app = Flask(__name__)

# set the name of the session cookie
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
# 會被覆蓋掉
app.secret_key = 'YOUR_SECRET_KEY'

# set the key for the token info in the session dictionary
TOKEN_INFO = 'token_info'

def get_currently_playing_track():
    try: 
        token_info = get_token()
    except:
        print('親 請登入')
        return redirect("/")

    sp = spotipy.Spotify(auth=token_info['access_token'])
    current_playing_track = sp.current_user_playing_track()['item']['name']
    print(f'SONG={current_playing_track}')
    # return 'GET SUCCESS'
    return current_playing_track

def get_users_top_artist():
    try: 
        token_info = get_token()
    except:
        print('親 請登入')
        return redirect("/")

    sp = spotipy.Spotify(auth=token_info['access_token'])
    recent_top_artist = sp.current_user_top_artists(limit=50,time_range='medium_term')
    # 將 JSON 資料轉換為 Python 字典
    data_dict = recent_top_artist
    genres_data = []
    for item in data_dict['items']:
        genres_data.extend(item['genres'])
    # 將提取的資料轉換為 Pandas DataFrame
    df = pd.DataFrame({'Genres': genres_data})
    genre_counts = df['Genres'].value_counts()
    # 選擇統計大於3的類別
    filtered_genres = genre_counts[genre_counts > 3]
    result_json = {
    'name': [],
    'count': []
    }
    for genre, genre_counts in filtered_genres.items():
        result_json['name'].append(genre)
        result_json['count'].append(genre_counts)

    # 將結果轉為 JSON 格式
    final_json = json.dumps(result_json, ensure_ascii=False)
    return final_json


# route to handle logging in
@app.route('/')
def login():
    # create a SpotifyOAuth instance and get the authorization URL
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

# route to handle the redirect URI after authorization
@app.route('/redirect')
def redirect_page():
    # clear the session
    session.clear()
    # get the authorization code from the request parameters
    code = request.args.get('code')
    # exchange the authorization code for an access token and refresh token
    token_info = create_spotify_oauth().get_access_token(code)
    # save the token info in the session
    session[TOKEN_INFO] = token_info
    # redirect the user to the get_currently_playing_track route
    return redirect(url_for('to_home',_external=True))

# API-正在收聽
@app.route('/homepage')
def to_home():
    top_artist_data = get_users_top_artist()
    currently_playing_data = get_currently_playing_track()
    return render_template('index.html', top_50_artist=top_artist_data, current_track=currently_playing_data)
# def get_currently_playing_track():
#     try: 
#         token_info = get_token()
#     except:
#         print('親 請登入')
#         return redirect("/")

#     sp = spotipy.Spotify(auth=token_info['access_token'])
#     current_playing_track = sp.current_user_playing_track()['item']['name']
#     print(f'SONG={current_playing_track}')
#     # return 'GET SUCCESS'
#     return redirect(url_for('get_users_top_artist', _external=True))

# API-常聽50
# @app.route('/topArtists')
# def get_users_top_artist():
#     try: 
#         token_info = get_token()
#     except:
#         print('親 請登入')
#         return redirect("/")

#     sp = spotipy.Spotify(auth=token_info['access_token'])
#     recent_top_artist = sp.current_user_top_tracks(limit=5,time_range='medium_term')['total']
#     print(recent_top_artist)
#     return 'RECENT ARTIST SUCCESS'


# function to get the token info from the session
def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        # if the token info is not found, redirect the user to the login route
        redirect(url_for('login', _external=False))
    
    # check if the token is expired and refresh it if necessary
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = '933aabd552e544079c9f61182e35b8d6',
        client_secret = 'bc2813ce935545239693166c88c4a076',
        redirect_uri = url_for('redirect_page', _external=True),
        scope='user-library-read user-read-currently-playing user-top-read'
    )

app.run(debug=True)