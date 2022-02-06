from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters.onebot.v11.event import Event
import requests

miao=on_command("来个猫猫")
@miao.handle()
async def hf(bot:Bot,ev:Event):
    import requests
    img=requests.get("http://edgecats.net/")
    await bot.send(event=ev,message=MessageSegment.image(img.content))