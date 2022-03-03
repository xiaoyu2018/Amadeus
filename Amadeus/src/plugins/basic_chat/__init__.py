from nonebot import get_driver, on_command, on_message
from nonebot.params import CommandArg,EventMessage
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message,MessageSegment
from os.path import expanduser,join


data_path=join(expanduser('~'),"bot\chat_data.txt")

matcher1=on_message(priority=3)
matcher2=on_command("记忆",aliases={"ln"},priority=2)

@matcher1.handle()
async def basic_chat(matcher: Matcher,msg: Message = EventMessage()):
    chat_data=load_data(data_path)
    msg=str(msg)
    if(msg==None or msg==''):
        return
    if(msg in chat_data.keys()):
        
        await matcher.finish(Message(chat_data[msg]))


@matcher2.handle()
async def add_data(matcher: Matcher,msg: Message = CommandArg()):
    chat_data=load_data(data_path)
    s_msg=str(msg).split(" ")
    # print(s_msg.split(" "))
    chat_data[s_msg[0]]=" ".join(s_msg[1:])
    
    await save_data(data_path,chat_data)
    matcher.stop_propagation()
    await matcher.finish("边人记住了"+Message(MessageSegment.face(16)))

async def save_data(path:str,data:dict):
    with open(path,"w",encoding="utf-8") as f:
        for i in data.keys():
            f.write(i+" "+data[i]+"\n")

    # # 在服务器备份chatdata，防止部署新版本时丢失文件
    # try:
    #     with open("/root/bot/chat_data.txt.bak","w",encoding="utf-8") as f:
    #         for i in data.keys():
    #             f.write(i+" "+data[i]+"\n")
    # except:
    #     print("备份失败！")
        
def load_data(path:str):
    chat_data=dict()
    with open(path,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            data=[i.strip() for i in line.split(" ")]
            chat_data[data[0]]=" ".join(data[1:])
    return chat_data


