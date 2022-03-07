import sys
sys.path.append("/root/bot/Amadeus/src/")
from shared import spider
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message

matcher=on_command("热搜",aliases={"hot"},priority=2)

@matcher.handle()
async def PushAnswer(matcher: Matcher):
    matcher.stop_propagation()
    page_text =await spider.GetPage("https://top.baidu.com/board?tab=realtime","get")
    titles= await spider.ParsePage(page_text,'/html/body/div/div/main/div[2]/div/div[2]/div/div[2]/a/div[1]/text()')
    await matcher.send("====百度热搜榜Top30====")
    res=""
    for i in range(30):
        res+=Message(f"{i+1}. {titles[i]}\n")

    await matcher.finish(res)