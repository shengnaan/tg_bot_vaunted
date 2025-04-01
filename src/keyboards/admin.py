from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать Насте П сообщение", callback_data="send_to_nastya")
        ],
    ]
)

confirm_admin_send_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да!!!", callback_data="confirm_admin"),
            InlineKeyboardButton(text="Не, перепишу", callback_data="cancel_admin"),
        ],
    ]
)
