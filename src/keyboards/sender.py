from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirm_send_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да!!!", callback_data="confirm"),
            InlineKeyboardButton(text="Не, перепишу", callback_data="cancel"),
        ],
    ]
)
