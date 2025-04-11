from flask import Flask, render_template  # type: ignore
from gemini_retrieval import generateRoast
from spotify_retrieval import getData

app = Flask(__name__)

@app.route('/analysis')
def analysis_page():
    spotify_data = getData()
    

    roast = generateRoast()

    return render_template('Analysis.html', 
    artists = spotify_data[0],
    songs = spotify_data[1],
    roast=roast)

if __name__ == '__main__':
    app.run(debug=True)
