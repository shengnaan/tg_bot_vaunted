import random

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from core.config import Settings
from src.keyboards.vaunted import vaunted_keyboard

vaunted_router = Router()

@vaunted_router.message(
    Command("praise")
)
async def praise(message: Message) -> None:
    await message.answer(
        random.choice(Settings.PRAISES),
        reply_markup=vaunted_keyboard
    )


@vaunted_router.callback_query(
    F.data == "praise"
)
async def praise_(c: CallbackQuery) -> None:
    await c.answer()
    await c.message.edit_text(
        random.choice(Settings.PRAISES),
        reply_markup=vaunted_keyboard
    )
