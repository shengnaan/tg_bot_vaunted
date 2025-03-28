from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from core.config import Settings
from src.keyboards.sender import confirm_send_keyboard

sender_router = Router()


class SendStates(StatesGroup):
    waiting_for_msg = State()
    message = State()


@sender_router.message(
    Command("send")
)
async def send(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Напиши сообщение, которое хочешь отправить Пете п."
    )
    await state.set_state(SendStates.waiting_for_msg)


@sender_router.message(
    StateFilter(SendStates.waiting_for_msg)
)
async def process_send(message: Message, state: FSMContext) -> None:
    await message.answer(
        text="Отправляю Петьке это сообщение?"
    )
    await message.copy_to(
        message.chat.id,
        reply_markup=confirm_send_keyboard,
    )
    await state.update_data(message=message)


@sender_router.callback_query(
    F.data == "confirm"
)
async def confirm_resend(c: CallbackQuery, state: FSMContext) -> None:
    await c.answer()
    data = await state.get_data()
    msg = data["message"]
    await msg.copy_to(
        Settings.ADMIN_ID,
        reply_markup=ReplyKeyboardRemove(),
    )



@sender_router.callback_query(
    F.data == "cancel"
)
async def cansel_resend(c: CallbackQuery, state: FSMContext) -> None:
    await c.answer()
    await c.message.answer(
        text="Лаааадна, думай"
    )
    await state.clear()
