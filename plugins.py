"""
插件
"""
from math import *
import random
import requests
from controls import on_command, previlage
superuser = {861900161,925582364}  # 超级用户




@on_command('复读')
def echo(bot, ctx, arg):
    if previlage(superuser, ctx):
        return previlage(superuser, ctx)
    arg = arg.lstrip()
    if not arg:
        return {'reply': '空格要怎么复读？'}
    bot.send(ctx, arg)


@on_command('喵一个')
def miao(bot, ctx, arg):
    bot.send(ctx, '喵～')


@on_command('随机数')
def _(bot, ctx, arg):
    bot.send(ctx, str(random.randint(0, 100)))


@on_command('计算')
def _(bot, ctx, arg):
    expression = arg.strip()
    print(expression)
    bot.send(ctx, str(eval(expression)))


@on_command('知乎日报')
def _(bot, ctx, arg):
    STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'

    resp = requests.get(
        'https://news-at.zhihu.com/api/4/news/latest',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
    )

    data = resp.json()
    stories = data.get('stories')

    if not stories:
        bot.send(ctx, '暂时没有数据，或者服务无法访问')
        return

    reply = ''
    for story in stories:
        url = STORY_URL_FORMAT.format(story['id'])
        title = story.get('title', '未知内容')
        reply += f'\n{title}\n{url}\n'

    bot.send(ctx, reply)
