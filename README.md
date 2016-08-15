# 概述

用于将excel树形结构生成指定的XML文件，如下Excel：

![excel.jpg](excel.JPG)

生成XML为：

```
<?xml version="1.0" ?>
<NodeMap>
	<NodeMapItem Depth="1" ID="e5c80e50-6054-11e6-a14b-083e8e5f5446" OperCode="1" Path="01" TagFilter="(TagName='01')" Title="01">
		<NodeMapItem Depth="2" ID="e5c80e51-6054-11e6-bc24-083e8e5f5446" OperCode="1-1" Path="0101" TagFilter="(TagName='0101')" Title="0101">
			<NodeMapItem Depth="3" ID="e5c80e52-6054-11e6-a6be-083e8e5f5446" OperCode="1-1-1" Path="010101" TagFilter="(TagName='010101')" Title="010101"/>
			<NodeMapItem Depth="3" ID="e5c83568-6054-11e6-9f18-083e8e5f5446" OperCode="1-1-2" Path="010102" TagFilter="(TagName='010102')" Title="010102"/>
		</NodeMapItem>
		<NodeMapItem Depth="2" ID="e5c83569-6054-11e6-a579-083e8e5f5446" OperCode="1-2" Path="0102" TagFilter="(TagName='0102')" Title="0102">
			<NodeMapItem Depth="3" ID="e5c8356a-6054-11e6-a34d-083e8e5f5446" OperCode="1-2-1" Path="010201" TagFilter="(TagName='010201')" Title="010201"/>
			<NodeMapItem Depth="3" ID="e5c8356b-6054-11e6-9bd1-083e8e5f5446" OperCode="1-2-2" Path="010202" TagFilter="(TagName='010202')" Title="010202"/>
		</NodeMapItem>
	</NodeMapItem>
</NodeMap>
```

# 使用

直接运行`Generate.py`脚本即可，会根据`config.py`文件的配置生成xml文件

# 配置

`config.py`文件配置如下：

```
CONFIG = [
    {
        'EXCEL_PATH': './*.xlsx',
        'OUTPUT_PATH': './%(filename)s.xml',
        'MAX_DEPTH': 5,
        'START_ROW': 3
    }
]
```

`CONFIG`数组变量每一个元素为字典对象，配置相应的参数

 - `EXCEL_PATH`: 配置excel文件路径，支持'*'通配符的使用
 - `OUTPUT_PATH`: 配置相应的导出文件路径，支持格式化参数`%(filename)s`表示对应文件名称
 - `MAX_DEPTH`: 树结构的最大深度，即Excel中的前几列为树结构
 - `START_ROW`: 生成xml时跳过Excel中的前几行