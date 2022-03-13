import sys
import os
path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message,MessageSegment
from nonebot.params import CommandArg


from shared.spider import GetJson

mathcer=on_command("缩写",aliases={"sx"},priority=2)

@mathcer.handle()
async def PushAnswer(matcher: Matcher,msg: Message = CommandArg()):
    matcher.stop_propagation()
    l=await GetJson("https://lab.magiconch.com/api/nbnhhsh/guess","post",data={"text":f"{msg}"})
    res=""
    for d in l:
        res+=Message(f"====={d['name']}=====\n")
        if('trans' in d.keys()):
            res+=Message("\n".join([f"{i+1}. {s}" for i,s in enumerate(d['trans'])])+"\n")
        else:
            res+=Message("啥意思啊？我不道啊！")
    
    await matcher.finish(res)


if __name__=='__main__':
    
    pass
