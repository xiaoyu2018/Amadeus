from cmath import sin,cos,tan,sqrt,exp,acos,asin,atan,log
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message,MessageSegment

matcher=on_command("计算",aliases={"calc"},priority=2)

@matcher.handle()
async def calculate(matcher: Matcher,msg: Message = CommandArg()):
    s_msg=str(msg)
    
    res=""
    if(not is_safe(str(s_msg))):
        res=Message.template(
        "参数包含非法字符串{}"
    ).format(MessageSegment.face(96))
    else:
        try:
            res=str(eval(s_msg))
        except Exception as e:
            print(e)
            res="看不懂"+Message(MessageSegment.face(178))
    matcher.stop_propagation()
    await matcher.finish(res)
    
def is_safe(msg):
    stop_words=[
        "import","os","sys","system","on_command","matcher",
        "CommandArg","Message","MessageSegment","Matcher"
    ]
    
    for i in stop_words:
        if i in msg:
            return False
    return True

