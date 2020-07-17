import requests

data = requests.get(url='http://geoportal.rcmrd.org/geoserver/wms?request=getCapabilities&service=wms&version=1.3.0')
print(data.text)


@app.route('/ogc')
def route_wms():
    url = request.args.get('url')
    try:
        data = requests.get(url=url)
        return data.text
    except Exception as e:
        return e