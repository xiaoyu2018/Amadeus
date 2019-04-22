"""
这个模块用于接收 酷Q 消息，并调用对应命令的处理函数
"""
from config import *
only_to_me = True

bot = CQHttp(api_root=api_root)

def only_u(flag1, msg):
    flag2=0
    if '[CQ:at,qq=1942160845] ' in msg:
        msg = msg[len('[CQ:at,qq=1942160845] '):]
        flag2=1
    if flag1==1 and flag2 == 0:
        return
    return msg 
    

# 注册私聊消息处理函数
@bot.on_message('group')
def handle_msg(ctx):
    pprint(ctx)
    msg: str=only_u(only_to_me, ctx['message'])
    # msg: str = ctx['message']
    sp = msg.split(maxsplit=1)
    if not sp:
        return {'reply':'你只发空格是什么意思？'}
    cmd, *remained = sp
    arg = ''.join(remained)
    # print('cmd:', cmd)
    # print('arg:', arg)
    handler = command_handlers.get(cmd)
    # print('handler:', handler)

    if handler:
        return handler(bot, ctx, arg)
    else:                                          #图灵机器人万金油回复
        replies = tuling.get_reply(msg)
        if replies:
            return {'reply': replies[0]}


bot.run(Ip, port)
