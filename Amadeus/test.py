import requests 

Headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"Content-Length": "279",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Host": "fanyi.youdao.com",
"Origin": "https://fanyi.youdao.com",
"Referer": "https://fanyi.youdao.com/",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform": "Windows",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"X-Requested-With": "XMLHttpRequest"
}

'''

'''

Data={
    "i":"你在干什么",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16468116925454",
    "sign": "d937343f7b384f36e2757f61691ced7f",
    "lts": "1646811692545",
    "bv": "6ea3c8fa8c34ed9c526a7795290401ab",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}
req=requests.post("https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",headers=Headers,data=Data)

print(req.text)