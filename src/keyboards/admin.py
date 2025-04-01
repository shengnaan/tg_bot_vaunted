from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать Насте П сообщение", callback_data="send_to_nastya")
        ],
    ]
)
