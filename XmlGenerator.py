# encoding: UTF-8

import xml.etree.ElementTree as elementtree

from xml.etree.ElementTree import Element
from xml.dom.minidom import parseString
from uuid import uuid1

class XmlGenerator:
    def __init__(self, data):
        self.element = self.Generator(data)

    def __str__(self):
        return self.prettyoutput(self.element)

    def prettyoutput(self, element):
        xml = parseString(elementtree.tostring(element))
        return xml.toprettyxml()

    def Generator(self, data):
        root = Element(data['tag'])
        for i in range(0, len(data['children'])):
            root.append(self.GenerateElement(data['children'][i], 0, str(i + 1)))
        return root


    def GenerateElement(self, data, depth, opercode):
        element = Element(data['tag'], {
            'ID': str(uuid1()),
            'Title': data['name'],
            'OperCode': opercode,
            'TagFilter': '(TagName=\'%s\')' % data['name'],
            'Path': data['name'],
            'Depth': str(depth + 1)
        })
        for i in range(0, len(data['children'])):
            element.append(self.GenerateElement(data['children'][i], depth + 1, '%s-%s' % (opercode, i + 1)))
        return element


if __name__ == '__main__':
    data = {'children': [{'children': [
        {'children': [{'children': [], 'name': '010101', 'tag': 'NodeMapItem'}], 'name': '0101', 'tag': 'NodeMapItem'},
        {'children': [{'children': [], 'name': '010201', 'tag': 'NodeMapItem'}], 'name': '0102', 'tag': 'NodeMapItem'}],
                          'name': '01', 'tag': 'NodeMapItem'}], 'name': '', 'tag': 'NodeMap'}
    element = Generator(data)
    xml = elementtree.dump(element)
    # xml = elementtree.tostring(element)
    print(xml)

