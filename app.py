from flask import Flask ,  request
import requests


app = Flask(__name__)
@app.route('/')
def route_wms():
    url = request.args.get('url')
    data = requests.get(
        url=url)
    return data.text

if __name__ == '__main__':
    app.run(debug=True)

