from aiogram.filters import BaseFilter
from aiogram.types import Message


class AdminFilter(BaseFilter):
    def __init__(self) -> None:
        self.allowed_users = [773812717]

    async def __call__(self, message: Message) -> bool:
        return not message.from_user.id not in self.allowed_users
