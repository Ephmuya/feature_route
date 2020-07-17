from flask import Flask,request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return 'ok'

@app.route('/geoserver')
def rcmrd():
    url = request.args.get('url')
    try:
        data = requests.get(url=url)
        return data.text
    except Exception as e:
        return e

if __name__ ==  ('__main__'):
    app.run(debug= True)

