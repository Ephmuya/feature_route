from flask import Flask,request,Response
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
        data = data.text
        base = request.base_url
        update_base = data.replace("http://geoportal.rcmrd.org", base+"/http://geoportal.rcmrd.org")
        return Response(update_base, mimetype='text/xml')
    except Exception as e:
        return e

if __name__ ==  ('__main__'):
    app.run(debug= True)

