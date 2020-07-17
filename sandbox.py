import requests
import lxml.etree as ET

data = requests.get(url='http://geoportal.rcmrd.org/geoserver/wms?request=getCapabilities&service=wms&version=1.3.0')
data = data.text
update_base = data.replace("http://geoportal.rcmrd.org", "https://geoportal.rcmrd.org")
print(update_base)



