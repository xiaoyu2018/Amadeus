from nonebot import get_driver
from .config import Config
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message,MessageSegment


global_config = get_driver().config
plugin_config = Config(**global_config.dict())

# print(plugin_config.bs_uids)

matcher1=on_command("动态",priority=2)

# 获取指定用户动态
matcher1.handle()
async def dynamic():
    pass
