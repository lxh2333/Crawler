import requests
from Py4Js import *
import json

# 谷歌翻译方法
def google_translate(content):
    js = Py4Js()
    tk = js.getTk(content)


    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "cookie": "_ga=GA1.3.2048479516.1562760361; NID=187=T63hZKcoTxZGAGxh8zVCz6rWhU4qLJTK4N_SCOXj_D1_qt9IdcVs_FJSqzhiMQakOLEN6qSHXS0mGPyWbOAZq7rtBEyKo1al9N7aCYOq0XmA52UZDtjfBsOOcVySvk59qWwUeEW1JCTYZBk94dFIBkR60XlAB1ILw636vgUjdyM; _gid=GA1.3.818230598.1574668912; 1P_JAR=2019-11-25-15"
    }
    param = {
        'client': 'webapp',
        'sl':'en',
        'tl':'zh-CN',
        'hl':'zh-CN',
        'dt':'at',
        'dt':'bd',
        'dt':'ex',
        'dt':'ld',
        'dt':'md',
        'dt':'qca',
        'dt':'rw',
        'dt':'rm',
        'dt':'ss',
        'dt':'t',
        'otf':'1',
        'pc':'1',
        'ssel':'3',
        'tsel':'3',
        'kc':'2',
        'tk': tk,
        'q': content
    }

    result = requests.get("https://translate.google.cn/translate_a/single", params=param, headers=headers)

    # 返回的结果为Json，解析为一个嵌套列表

    trans = result.json()[0]
    ret = ''
    for i in range(len(trans)):
        line = trans[i][0]
        if line != None:
            ret += trans[i][0]
    return ret



