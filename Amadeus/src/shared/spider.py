import requests
from lxml import etree

HEADERS={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55'
}


async def GetPage(url:str,method:str,data:dict=None,params:dict=None):

    res=""
    try:
        res=requests.request(method,url,data=data,headers=HEADERS,params=params).text
    except Exception as e:
        res=None
    
    return res

async def GetJson(url:str,method:str,data:dict=None,params:dict=None):
    res=dict

    try:
        res=requests.request(method,url,data=data,headers=HEADERS,params=params).json()
    except Exception as e:
        res=None
    return res

async def ParsePage(page_text:str,pattern:str):
    res=[]
    try:
        tree=etree.HTML(page_text,None)
        res=tree.xpath(pattern)
    except:
        res=[]
    return res


if __name__=='__main__':
    pass
    