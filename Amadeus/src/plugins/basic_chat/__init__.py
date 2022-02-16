from nonebot import get_driver, on_command, on_message,rule
from nonebot.params import EventPlainText,CommandArg
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from .config import Config

global_config = get_driver().config
plugin_config = Config(**global_config.dict())

matcher1=on_message(rule=rule.to_me(),priority=3)
matcher2=on_command("记忆",aliases={"lrn"},rule=rule.to_me(),priority=2)

@matcher1.handle()
async def basic_chat(matcher: Matcher,msg: str = EventPlainText()):
    chat_data=load_data(plugin_config.bc_data_path)
    if(msg in chat_data.keys()):
        await matcher.finish(chat_data[msg])
    await matcher.finish("666")

@matcher2.handle()
async def Add_Data(matcher: Matcher,msg: Message = CommandArg()):
    chat_data=load_data(plugin_config.bc_data_path)
    s_msg=str(msg).split(" ")
    # print(s_msg.split(" "))
    chat_data[s_msg[0]]=" ".join(s_msg[1:])
    
    await save_data(plugin_config.bc_data_path,chat_data)
    matcher.stop_propagation()
    await matcher.finish("边人记住了")

async def save_data(path:str,data:dict):
    with open(path,"w",encoding="utf-8") as f:
        for i in data.keys():
            f.write(i+" "+data[i]+"\n")
        
def load_data(path:str):
    chat_data=dict()
    with open(path,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            data=[i.strip() for i in line.split(" ")]
            chat_data[data[0]]=" ".join(data[1:])
    return chat_data

