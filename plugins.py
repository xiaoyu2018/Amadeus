from math import *


#基础的聊天功能
def basictalk(msg):
    flag = 0
    msg=msg.strip()
    if'吗' in msg or '?' in msg or '？' in msg:
        flag = 1
        msg = msg.replace('?', '')
        msg = msg.replace('吗', '')
        msg = msg.replace('？', '')
        msg += '!'
    if msg[0] == '你':
        flag = 1
        msg = '我'+msg[1:]
    if flag == 0:
        return '不知道你在讲什么!'
    return msg

#复读机
def echo(msg):
    msg = msg.replace('复读', '')
    return msg.lstrip()

#计算器
def calculator(msg):
    expression=msg[len('计算'):].strip()
    return str(eval(expression))   #eval是内置的求值函数
#测试单元
if __name__ == "__main__":
    a = '计算  132*123'
    print(calculator(a))
