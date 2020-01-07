import codecs
import urllib.request
import urllib.parse
import json

def read_txt():
    f = codecs.open('en.txt', 'rb', 'utf-8')
    content = f.read()
    print(content)
    f.close()
    return str(content)
def translate_baidu(content):
    baidu_url = 'http://fanyi.baidu.com/basetrans'
    data = {}

    data['from'] = 'en'
    data['to'] = 'zh'
    data['query'] = content
    data['transtype'] = 'translang'
    data['simple_means_flag'] = '3'
    data['sign'] = '94582.365127'
    data['token'] = 'ec980ef090b173ebdff2eea5ffd9a778'
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    baidu_re = urllib.request.Request(baidu_url, data, headers)
    baidu_response = urllib.request.urlopen(baidu_re)
    baidu_html = baidu_response.read().decode('utf-8')
    target2 = json.loads(baidu_html)

    trans = target2['trans']
    ret = ''
    for i in range(len(trans)):
        ret += trans[i]['dst'] + '\n'
    return ret
def translate():
    content_2 = "Huawei - Building a Fully Connected, Intelligent World"
    translate_1 = translate_baidu(content_2)
    print(translate_1)
translate()