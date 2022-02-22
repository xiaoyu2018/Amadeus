
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message,MessageSegment
from nonebot.params import CommandArg

URL="https://lab.magiconch.com/api/nbnhhsh/guess"

mathcer=on_command("缩写",priority=2)


async def Require(text):
    import requests
    
    req=requests
    res=req.post(url=URL,data={"text":f"{text}"})

    return res.json()
    

@mathcer.handle()
async def PushAnswer(matcher: Matcher,msg: Message = CommandArg()):
    matcher.stop_propagation()
    l=await Require(msg)
    res=""
    for d in l:
        res+=Message(f"====={d['name']}=====\n")
        if('trans' in d.keys()):
            res+=Message("\n".join([f"{i+1}. {s}" for i,s in enumerate(d['trans'])])+"\n")
        else:
            res+=Message("啥意思啊？我不道啊！")
    
    await matcher.finish(res)
    



if __name__=='__main__':
    # l=Require("asdada")
    # print(foo(l))
    pass
