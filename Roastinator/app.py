from flask import Flask, render_template, session, redirect, url_for, request  # type: ignore
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
from gemini_retrieval import generateRoast
from spotify_retrieval import getData 

app = Flask(__name__)
app.secret_key = os.urandom(64)

SPOTIFY_CLIENT_ID = os.environ.get('CLIENT_KEY')
SPOTIFY_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = 'user-top-read'


@app.route('/')
def title_screen():
    return render_template('TitleScreen.html')

@app.route('/login')
def login():
    sp_oauth = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True
    )
    
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    )
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    session['token_info']= {
        'access_token': token_info['access_token'],
        'refresh_token': token_info['refresh_token'],
        'expires_at': token_info["expires_at"]}
    return redirect(url_for('loading'))



@app.route('/loading')
def loading():
    if 'token_info' not in session:
        return redirect(url_for('login'))
    
    return render_template('LoadingScreen.html')


@app.route('/analysis')
def analysis():
    try:
        if 'token_info' not in session:
            return redirect(url_for('login'))
        access_token = session['token_info']['access_token']
        spotify_data = getData(access_token)
        roast = generateRoast(access_token)

        return render_template('Analysis.html', 
            artists=spotify_data[0],
            songs=spotify_data[1],
            roast=roast
        )

    except Exception as e:  # <- This EXCEPT must align with TRY
        print(f"ANALYSIS ERROR: {str(e)}")
        session.clear()
        return redirect(url_for('login'))


@app.route('/signout')
def signout():
    # Clear all session data
    session.clear()
    # Delete Spotify token cache
    if os.path.exists('.cache'):
        os.remove('.cache')
    return redirect(url_for('title_screen'))

if __name__ == '__main__':
    app.run(debug=True)