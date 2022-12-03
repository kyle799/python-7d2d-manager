import xml.etree.ElementTree as elemettree

serverConfigRoot="c:\\users\\kyle\\\desktop\\7D2D"
defaultServerConfig=serverConfigRoot+"\\serverconfig.xml"

configTree=elemettree.parse(defaultServerConfig)
configRoot=configTree.getroot()
for property in configRoot.iter('property'):
    print(f"{property.attrib['name']},{property.attrib['value']}")