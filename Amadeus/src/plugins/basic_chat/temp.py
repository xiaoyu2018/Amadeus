from nonebot.adapters import MessageSegment

class MyMessageSegment(MessageSegment):
    def __str__(self) -> str:
        return super().__str__()
    
    def get_message_class(self):
        pass
    def is_text(self) -> bool:
        return super().is_text()
