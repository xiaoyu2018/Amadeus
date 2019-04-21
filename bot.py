from config import *


bot = CQHttp(api_root=apiroot)




@bot.on_message('group')             #将以下函数注册为私聊
def HandleMessage(ctx):
    #print(ctx)
    msg=ctx['message']
    if msg[0:2]=='复读':
        msg=echo(msg)
    elif '随机'in msg or '随机数' in msg:
        msg=str(random.randint(1,100))
    elif msg[0:2]=='计算':
        msg=calculator(msg)
    else:
        msg=basictalk(msg)
    bot.send(ctx,msg)
    
bot.run(host,port)              #循环监听酷q传来的消息




