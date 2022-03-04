from email import message
import nonebot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from nonebot import require
from .config import Config

global_config = nonebot.get_driver().config
# nonebot.logger.info("global_config:{}".format(global_config))
plugin_config = Config(**global_config.dict())
# nonebot.logger.info("plugin_config:{}".format(plugin_config))
# 加载官方定时任务插件
scheduler = require("nonebot_plugin_apscheduler").scheduler  # type:AsyncIOScheduler

# 发送时间
times=[{"hour":7,"min":30},{"hour":12,"min":1}]
async def send_everyday():
    
    message2="别忘上工程伦理！！！"

     # 给qq好友发消息
    for qq in plugin_config.npd_qq_friends:
        await nonebot.get_bot().send_private_msg(user_id=qq, message="")
    # 给群发消息
    for qq_group in plugin_config.npd_qq_groups:
        # await nonebot.get_bot().send_group_msg(group_id=qq_group, message=message1)
        await nonebot.get_bot().send_group_msg(group_id=qq_group, message="[CQ:at,qq={}]{}".format(861900161, message2))

# 调试
# scheduler.add_job(send_everyday, "interval", seconds=2, id="3213")

# 根据配置的参数，注册定时任务,每天发送
for index, time in enumerate(times):
    scheduler.add_job(send_everyday, "cron", hour=time["hour"], minute=time["min"], id=str(index))