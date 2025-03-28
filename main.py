import asyncio
import contextlib

from aiogram.methods import DeleteWebhook

from core.config import Settings
from src.routers.base_router import base_router
from src.scripts.bot import bot, dp


async def main() -> None:
    dp.include_router(base_router)
    await bot.set_my_commands(Settings.MENU_COMMANDS)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
