"""
这个模块用于提供注册命令的装饰器，和保存注册后的命令处理函数
"""

command_handlers = {}  # 键是命令名字，值是命令处理函数
        #是否只回复被@的消息

def on_command(name):
    """
    用于将函数注册为命令

    :param name: 命令名
    """

    def decorator(func):
        command_handlers[name] = func
        return func

    return decorator



def previlage(superuser, ctx):
    if ctx['sender']['user_id'] not in superuser:
        return {'reply':'只有超级用户才能使用此功能!'}