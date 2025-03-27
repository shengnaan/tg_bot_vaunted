import traceback

from aiogram import Router
from aiogram.types import ErrorEvent

from core.logger import logger

error_router = Router()


@error_router.errors()
async def error_handler(error: ErrorEvent) -> bool:
    """Глобальное логирование всех ошибок"""
    error_message = f"""
    ❌ Ошибка в боте!
    🔹 Тип: {type(error.exception).__name__}
    🔹 Сообщение: {error.exception}
    🔹 Апдейт: {error.update}
    🔹 Трассировка:
    {traceback.format_exc()}
    """
    logger.error(error_message)
    return True
