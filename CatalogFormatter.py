# encoding: UTF-8

from openpyxl import load_workbook
from XmlGenerator import XmlGenerator


class CatalogFormatter:
    def __init__(self, excelpath, outputpath, max_depth, start_row=0):
        self.excelpath = excelpath
        self.outputpath = outputpath
        self.max_depth = max_depth
        self.start_row = start_row
        wb = load_workbook(excelpath)
        ws = wb.active
        self.columns = tuple(ws.columns)
        self.data = {
            'tag': 'NodeMap',
            'name': '',
            'children': self.getchildren(0, self.start_row, len(self.columns[0]) - 1)
        }

    def getchildren(self, depth, fromindex, toindex):
        children = []
        if depth < max_depth:
            name = None
            for i in range(fromindex, toindex + 1):
                if self.columns[depth][i].value or i == toindex:
                    if name:
                        children.append({
                            'tag': 'NodeMapItem',
                            'name': name,
                            'children': self.getchildren(depth + 1, start, i if i == toindex else i - 1)
                        })
                        if self.columns[depth][i].value and i == toindex:
                            children.append({
                                'tag': 'NodeMapItem',
                                'name': self.columns[depth][i].value,
                                'children': self.getchildren(depth + 1, start, i)
                            })
                    name = self.columns[depth][i].value
                    start = i
        return children


    def generatorxml(self):
        generator = XmlGenerator(self.data)
        self.xml = str(generator)
        print(self.xml)

    def outputfile(self):
        self.generatorxml()
        file = open(self.outputpath, 'wb')
        file.write(self.xml.encode('utf-8'))
        file.flush()
        file.close()

if __name__ == '__main__':
    ExcelPath = r'C:\Users\baiya\Desktop\资源目录2版 - 副本Formatted.xlsx'
    outputpath = r'C:\Users\baiya\Desktop\catalog.xml'
    max_depth = 5

    catalogFormatter = CatalogFormatter(ExcelPath, outputpath, max_depth, 3)
    catalogFormatter.outputfile()