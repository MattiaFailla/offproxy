from flask import Flask
import urllib.request
import urllib.parse

app = Flask(__name__)


@app.route("/<int:id>")
def home(id):
    url = 'https://world.openfoodfacts.org/api/v0/product/'+str(id)+'.json'
    f = urllib.request.urlopen(url)
    data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=True)