import requests
from lxml import etree
URL="https://top.baidu.com/board?tab=realtime"
HEADERS={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55'
}

async def get_content():
    req=requests

    res=req.get(url=URL,headers=HEADERS)
    tree=etree.HTML(res.text,None)
    titles=tree.xpath('/html/body/div/div/main/div[2]/div/div[2]/div/div[2]/a/div[1]/text()')
    # links=tree.xpath('/html/body/div/div/main/div[2]/div/div[2]/div/div[2]/a/@href ')

    return titles #,links[:15]

if __name__=='__main__':
    print()