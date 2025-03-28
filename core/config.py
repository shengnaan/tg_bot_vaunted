import os

from aiogram.types import BotCommand
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TOKEN = os.getenv("TOKEN")
    PRAISES = ["лув киска, пока пуста, заполню как смогу"]
    CAT_TAGS = ["cute", "funny", "sleepy", "play", "adorable"]
    MENU_COMMANDS = [
        BotCommand(command="/menu", description="Главное меню"),
        BotCommand(command="/meow", description="Картинка с китиком"),
        BotCommand(command="/praise", description="Похвалить"),
        BotCommand(command="/send", description="Написать пете п.")
    ]
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
