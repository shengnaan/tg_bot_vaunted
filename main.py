import asyncio
import contextlib

from aiogram.methods import DeleteWebhook

from src.routers.base_router import bot, dp


async def main() -> None:
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
