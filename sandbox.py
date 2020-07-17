import requests

data = requests.get(url='http://geoportal.rcmrd.org/geoserver/wms?request=getCapabilities&service=wms&version=1.3.0')
print(data.text)