from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from src.routers.error import error_router
from src.routers.src.admin.base_router import base_admin_router
from src.routers.src.pictures import pictures_router
from src.routers.src.sender import sender_router
from src.routers.src.vaunted import vaunted_router

base_router = Router()


@base_router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Настя П(елёвина) привет!\n"
        "Это бот специально, чтоб напомнить тебе, что ты у меня самая самая!!!\n\n"
        "Бесконечно люблю!"
    )
    await message.answer(
        "Чтобы узнать все возможности Лаудика отправь /menu"
    )


@base_router.message(Command("menu"))
async def menu(message: Message) -> None:
    await message.answer(
        "1️⃣ /menu - главный босс, расскажет по понятиям кто за что базарит.\n\n"
        "2️⃣ /praise - это мастхев лаудика, тыкай и он напомнит тебе "
        "кто тут самый мили цветочек.\n\n"
        "3️⃣ /meow - в простонародье мяу или мээээу, Лаудик закинет тебе "
        "китикета. Будет он мили, игривый или смешной он решит сам.\n\n"
        "4️⃣ /send - отправить смс(очку) папочке (пете п.), кидай че "
        "хочешь, хоть смайлик, хоть фильм загрузи.\n\n"
        "балдей малыха"
    )


base_router.include_routers(
    error_router,
    vaunted_router,
    pictures_router,
    sender_router,
    base_admin_router
)
