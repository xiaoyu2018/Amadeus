from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message,MessageSegment
from .spider import get_content

matcher=on_command("热搜",aliases={"hot"},priority=2)

@matcher.handle()
async def PushAnswer(matcher: Matcher):
    matcher.stop_propagation()
    titles =await get_content()
    await matcher.send("====百度热搜榜Top30====")
    res=""
    for i in range(30):
        res+=Message(f"{i+1}. {titles[i]}\n")

    await matcher.finish(res)