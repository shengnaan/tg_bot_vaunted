import aiohttp
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BufferedInputFile, Message

from src.scripts.utils import get_url_with_random_tag

pictures_router = Router()


@pictures_router.message(Command("meow"))
async def meow(message: Message) -> None:
    msg = await message.reply("Ищу кота...")
    print(msg.from_user.id)
    await msg.delete()
    try:
        async with (
            aiohttp.ClientSession() as session,
            session.get(get_url_with_random_tag()) as resp
        ):
            if resp.status == 200:
                photo = await resp.read()
                await message.answer_photo(
                    photo=BufferedInputFile(
                        file=photo,
                        filename="cat.png"
                    )
                )
                await msg.delete()
            else:
                await message.answer("Не получилось найти котиков 🐾. Наверное они шпят...")
    except Exception:
        await message.answer("Произошла ошибка. Котики в отпуске 😿")
