from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

vaunted_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Похвалить еще раз🔄", callback_data="praise")],
    ]
)
