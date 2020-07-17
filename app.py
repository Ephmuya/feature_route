from flask import Flask ,  request
import requests


app = Flask(__name__)
@app.route('/')
def index():
    return 'ok'

@app.route('/ogc')
def route_wms():
    url = request.args.get('url')
    try:
        data = requests.get(url=url)
        return data.text
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(debug=True)

