import os
import sqlite3

from flask import Flask
from flask import g
from flask import send_from_directory
from flask_cors import CORS
import folium

from routes import authentication

app = Flask(__name__)
CORS(app)

app.register_blueprint(authentication.authentication)

basedir = os.path.abspath(os.path.dirname(__file__))


@app.errorhandler(404)
def page_not_found(e):
    return 'HTTP 404 Not Found', 404


@app.get('/status')
def status():
    return 'Bonsoir Giga Chad'


@app.route('/map')
def render_map():
    # create map object
    m = folium.Map(location=[48.6689443, 6.1552047], zoom_start=16, tiles="Stamen Terrain")
    # create marker
    folium.Marker(location=[48.6689443, 6.1552047], popup="Giga Chad", tooltip="Giga Chad").add_to(m)
    carte = m._repr_html_()
    return carte


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/hooktest', methods=['POST'])
def hook_root():
    os.execlp('kill', 'kill', '1')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5454, debug=True)
