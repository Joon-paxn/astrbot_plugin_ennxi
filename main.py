from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("ennxi_plugin", "Ennxi", "ennxi", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("helloworld")
    async def helloworld(self, event: AstrMessageEvent):
        """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息

    # 注册指令的装饰器。指令名为 info。注册成功后，发送 `/info` 就会触发这个指令
    @filter.command("info")
    async def info(self, event: AstrMessageEvent):
        """获取系统信息指令"""
        info_content = "内核：AstrBot\nPython版本: 3.10\n插件版本: v 1.0\n已载插件：49"
        yield event.plain_result(info_content)

    @filter.command("菜单")
    async def menu(self, event: AstrMessageEvent):
        """这是一个菜单指令"""
        menu_content = "1. 狼人杀\n2. 聊天\n3. 海龟汤\n4. 每日老婆\n5. 代码图片生成\n6. 表情包生成\n7. Minecraft Skin 查询\n8. 左轮手枪对决"
        yield event.plain_result(menu_content)