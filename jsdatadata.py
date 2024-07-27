import json
import time
# 打开 JSON 文件

# with open('webtext2019zh/web_text_zh_testa.json', 'r') as file:
# with open('webtext2019zh/web_text_zh_valid.json', 'r') as file:
delstr=["<strong>", "<aclass", "<b>", "<u>", "<blockquote>", "<li>", "<il>", "<ol>", "<aclass", "aclass", "ltlt", "gtgt", "<br>", "<img src", "<img", "data", " ", "-"]
with open('webtext2019zh/web_text_zh_train.json', 'r') as file:
    # 逐行读取 JSON 数据
    for line in file:
        # 解析每一行的 JSON 数据
        data = json.loads(line)
        # 对每一行的 JSON 数据进行处理
        # 例如，打印其中的某个字段
        # print(data)
        tmpstr=data['title']+"\n"+data['desc']+"\n"+data['content']
        for s in delstr:
            tmpstr.replace(s,'')
        print(tmpstr)
        # time.sleep(10000)