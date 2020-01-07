import codecs
import urllib.request
import urllib.parse
import json
import re
def read_txt():
    f = codecs.open('en.txt', 'rb', 'utf-8')
    content = f.read()
    print(content)
    f.close()
    return str(content)
def translate(content):
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1525141473246'
    data['sign'] = '47ee728a4465ef98ac06510bf67f3023'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    youdao_response = urllib.request.urlopen(youdao_url, data)
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)

    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        f = codecs.open('en_tran.txt', 'a', 'utf-8')
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
            print(line)
            if line != None:
                f.write(line+'\n')
        f.close()



def trans():
    content_1 = read_txt()
    translate(content_1)

trans()