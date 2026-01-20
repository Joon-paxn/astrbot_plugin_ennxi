from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.message_components import *
import sys
import requests
import json
import time

@register("ennxi_plugin", "Ennxi", "ennxi", "1.2.1")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("helloworld")
    async def helloworld(self, event: AstrMessageEvent):
        """这是一个 hello world 指令"""
        user_name = event.get_sender_name()
        message_str = event.message_str
        message_chain = event.get_messages()
        logger.info(message_chain)
        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!")

    # 注册指令的装饰器。指令名为 info。注册成功后，发送 `/info` 就会触发这个指令
    @filter.command("info")
    async def info(self, event: AstrMessageEvent):
        """获取系统信息指令"""
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        info_content = f"内核：AstrBot\nPython版本: {python_version}\n插件版本: v 1.0\n已载插件：53"
        yield event.plain_result(info_content)

    # 注册指令的装饰器。指令名为 菜单。注册成功后，发送 `/菜单` 就会触发这个指令    
    @filter.command("菜单")
    async def menu(self, event: AstrMessageEvent):
        """这是一个菜单指令"""
        menu_content = "1. 狼人杀\n2. 聊天\n3. 海龟汤\n4. 每日老婆\n5. 代码图片生成\n6. 表情包生成\n7. Minecraft Skin 查询\n8. 左轮手枪对决\n9.今日运势\n可以使用/菜单 答应数字来查询功能"
        yield event.plain_result(menu_content)

    # 这个是菜单的子命令1
    @filter.command("菜单 1")
    async def menu1(self, event: AstrMessageEvent):
        """这是一个菜单1指令"""
        menu_content = "狼人杀需要9个玩家然后添加队伍进行游戏"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令2
    @filter.command("菜单 2")
    async def menu2(self, event: AstrMessageEvent):
        """这是一个菜单2指令"""
        menu_content = "聊天功能可以和其他玩家进行聊天"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令3
    @filter.command("菜单 3")
    async def menu3(self, event: AstrMessageEvent):
        """这是一个菜单3指令"""
        menu_content = "海龟汤功能可以生成随机的海龟汤然后去解答"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令4
    @filter.command("菜单 4")
    async def menu4(self, event: AstrMessageEvent):
        """这是一个菜单4指令"""
        menu_content = "每日老婆功能可以每日在你的群里面抽取20位幸运群友作为你的老婆！"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令5
    @filter.command("菜单 5")
    async def menu5(self, event: AstrMessageEvent):
        """这是一个菜单5指令"""
        menu_content = "代码图片生成功能可以生成包含代码的图片"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令6
    @filter.command("菜单 6")
    async def menu6(self, event: AstrMessageEvent):
        """这是一个菜单6指令"""
        menu_content = "表情包生成功能可以生成的整蛊或者有意思的表情包"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令7
    @filter.command("菜单 7")
    async def menu7(self, event: AstrMessageEvent):
        """这是一个菜单7指令"""
        menu_content = "Minecraft Skin 查询功能可以查询玩家的 Minecraft 皮肤"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令8
    @filter.command("菜单 8")
    async def menu8(self, event: AstrMessageEvent):
        """这是一个菜单8指令"""
        menu_content = "左轮手枪对决功能可以和其他玩家进行左轮手枪对决"
        yield event.plain_result(menu_content)
        
    # 这个是菜单的子命令9
    @filter.command("菜单 9")
    async def menu9(self, event: AstrMessageEvent):
        """这是一个菜单9指令"""
        menu_content = "今日运势功能可以查询今日的运势 /今日运势"
        yield event.plain_result(menu_content)
    
    # 注册指令的装饰器。指令名为 enxi rs。注册成功后，发送 `/enxi rs` 就会触发这个指令
    @filter.command("enxi rs")
    async def enxi_rs(self, event: AstrMessageEvent):
        """获取ennxi.xyz网站统计数据"""
        try:
            # 发送HTTP GET请求到API地址
            response = requests.get("https://ennxi.xyz/api/stats.php?format=json&api_key=2e3f42e96211ad5de7f44697d706d38486e151ff20d29f8ffc3e7ecd206d210d")
            response.raise_for_status()  # 检查请求是否成功
            
            # 解析JSON响应
            data = response.json()
            
            # 提取所需数据
            total_visits = data.get("total_visits", 0)
            today_visits = data.get("today_visits", 0)
            datetime = data.get("datetime", "未知")
            
            # 格式化响应内容
            result = f"总访问人数：{total_visits}\n今日访问人数：{today_visits}\n更新日期：{datetime}\n官網Url：https://ennxi.xyz"
            
            yield event.plain_result(result)
        except requests.exceptions.RequestException as e:
            # 处理网络请求错误
            logger.error(f"API请求失败: {e}")
            yield event.plain_result("获取数据失败，请稍后重试")
        except json.JSONDecodeError as e:
            # 处理JSON解析错误
            logger.error(f"JSON解析失败: {e}")
            yield event.plain_result("数据格式错误，请稍后重试")
        except Exception as e:
            # 处理其他未知错误
            logger.error(f"未知错误: {e}")
            yield event.plain_result("发生未知错误，请稍后重试")
    
    # 注册指令的装饰器。指令名为 testpingtext。注册成功后，发送 `/testpingtext` 就会触发这个指令
    @filter.command("testpingtext")
    async def testpingtext(self, event: AstrMessageEvent):
        """测试机器人回复速度"""
        # 记录命令接收时的起始时间
        start_time = time.time()
        
        # 执行必要的处理（在此场景中主要是计时）
        
        # 记录命令处理完成时的结束时间
        end_time = time.time()
        
        # 计算响应时间，保留1位小数
        response_time = round(end_time - start_time, 1)
        
        # 按照指定格式返回结果
        result = f"({response_time} @)"
        
        yield event.plain_result(result)
