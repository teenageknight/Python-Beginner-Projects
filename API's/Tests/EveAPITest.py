
import requests
import xml.dom.minidom

response = requests.get("https://api.evemarketer.com/ec/marketstat?typeid=584")

tree = response.text
xml = xml.dom.minidom.parseString(tree)
pretty_xml = xml.toprettyxml()


print(tree)

print(response.status_code)

with open('xmltest.xml', 'w') as f:
    f.write(pretty_xml)
