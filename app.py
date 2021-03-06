from flask import Flask
from flask import Response
from flask_cors import CORS
import urllib.request
import urllib.parse

app = Flask(__name__)
CORS(app)


@app.route("/<id>")
def home(id):
    url = 'https://world.openfoodfacts.org/api/v0/product/'+str(id)+'.json'
    f = urllib.request.urlopen(url)
    data = f.read()
    return Response(data, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)