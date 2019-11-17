import requests
import json
import jsonpath

def get_one_page(url):
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    res=requests.get(url,headers=header)
    res.encoding=res.apparent_encoding
    return res.text


def pares_msg(res):
    res = json.loads(res)
    msg_json = jsonpath.jsonpath(res, '$..resultData')
    print(msg_json)

    each_name=jsonpath.jsonpath(msg_json,'$..nameNoHtml')
    showtime=jsonpath.jsonpath(msg_json,'$..showtime')
    venue=jsonpath.jsonpath(msg_json,'$..venue')
    verticalPic=jsonpath.jsonpath(msg_json,'$..verticalPic')
    for i in range(29):
        print("节目:",each_name[i])
        print("时间:",showtime[i])
        print("地址:",venue[i])
        print("海报:",verticalPic[i])


def main():
    url="https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage=1&tn="
    res=get_one_page(url)
    pares_msg(res)

if __name__ == '__main__':
    main()