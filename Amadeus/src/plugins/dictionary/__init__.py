import sys
import os
path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from shared import spider

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message,MessageSegment
from nonebot.params import CommandArg

matcher=on_command("翻译",aliases={"trans"},priority=2)

@matcher.handle()
async def PushAnswer(matcher: Matcher,msg: Message = CommandArg()):
    matcher.stop_propagation()
    if(str(msg)==""):
        await matcher.finish(Message("？ 翻译啥呢"))
    
    page_text=await spider.GetPage("https://www.youdao.com/w/"+str(msg)+r"/","get")
    answers=[]
    
    l1=await spider.ParsePage(page_text,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/p/text()")
    l2=await spider.ParsePage(page_text,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/text()")
    l3=await spider.ParsePage(page_text,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[@id='ydTrans']/div/div/p[2]/text()")
    l4=await spider.ParsePage(page_text,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/p/span/a/text()")
    answers.extend(l1+l2+l3+l4)
    
    if(not answers):
        await matcher.finish(Message("说的是人话吗"+MessageSegment.face(14)))
    res=""
    res+=Message(f"原词（句）：{msg}\n\n结果=========\n")

    for i in answers:
        i=i.strip()
        if(i=='' or (i[0]=="[" and i[len(i)-1]=="]")):
            continue
        res+=Message(i+"\n")
 
    await matcher.finish(res)
    

if __name__=='__main__':
    
    pass