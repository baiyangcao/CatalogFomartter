# encoding: UTF-8

from pathlib import Path
from config import CONFIG
from CatalogFormatter import CatalogFormatter

if __name__ == '__main__':
    for config in CONFIG:
        for path in Path('.').glob(config['EXCEL_PATH']):
            # 读取配置
            excelpath = str(path.absolute())
            filename = path.name
            suffix = path.suffix
            outputpath = str(Path(config['OUTPUT_PATH'] % {
                'filename': filename.replace(suffix, '')
            }).absolute())
            max_depth = config['MAX_DEPTH']
            start_row = config['START_ROW']

            # 生成xml文件
            catalogformatter = CatalogFormatter(
                excelpath, max_depth, start_row
            )
            catalogformatter.outputfile(outputpath)
            print('生成xml文件%s成功！' % outputpath)
