from aiogram import Bot, Dispatcher

from core.config import Settings
from core.logger import logger

bot = Bot(
    token=Settings.TOKEN,
    logger=logger
)

dp = Dispatcher()

