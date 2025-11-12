import xml.etree.ElementTree as ET


countries = ['Canada', 'United States', 'Panama']
codes = ['CA', 'US', 'PA' ]
fname = '/tmp/vulnerable-countries.xml'

root = ET.Element("root")

for i in range(len(countries)):
    doc = ET.SubElement(root, 'country', node=codes[i], name=countries[i])
    tree = ET.ElementTree(root)
    tree.write(fname)
