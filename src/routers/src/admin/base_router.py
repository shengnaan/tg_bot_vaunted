from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from core.config import Settings
from src.keyboards.admin import admin_keyboard, confirm_admin_send_keyboard
from src.scripts.filters import AdminFilter

base_admin_router = Router()


class AdminStates(StatesGroup):
    waiting_for_msg = State()
    message = State()


@base_admin_router.message(
    Command("admin"), AdminFilter()
)
async def admin(message: Message) -> None:
    await message.answer(
        "Выбери, что хочешь сделать:",
        reply_markup=admin_keyboard
    )


@base_admin_router.callback_query(
    F.data == "send_to_nastya"
)
async def send_to_nastya(c: CallbackQuery, state: FSMContext) -> None:
    await c.answer()
    await c.message.answer("Отправь сообщение, которое хочешь отправить настене.")
    await state.set_state(AdminStates.waiting_for_msg)


@base_admin_router.message(
    StateFilter(AdminStates.waiting_for_msg)
)
async def send_confirm(m: Message, state: FSMContext) -> None:
    await m.delete()
    await m.answer(
        text="Отправляю настене это сообщение?"
    )
    await m.copy_to(
        m.chat.id,
        reply_markup=confirm_admin_send_keyboard,
    )
    await state.update_data(message=m)


@base_admin_router.callback_query(
    F.data == "confirm_admin",
)
async def confirm_resend(c: CallbackQuery, state: FSMContext) -> None:
    await c.answer()
    data = await state.get_data()
    msg = data["message"]
    await msg.copy_to(
        Settings.NASTYA_ID,
        reply_markup=ReplyKeyboardRemove(),
    )
    await c.message.delete()
    await c.message.answer("Отправил!")



@base_admin_router.callback_query(
    F.data == "cancel_admin",
)
async def cansel_resend(c: CallbackQuery, state: FSMContext) -> None:
    await c.answer()
    await c.message.delete()
    await c.message.answer(
        text="Лаааадна, думай"
    )
    await state.clear()
