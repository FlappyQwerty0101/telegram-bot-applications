from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from keyboards.reply import support_keyboard
from states.form import Form
from database.db import save_application

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет!\nЯ бот для сбора заявок", reply_markup=support_keyboard(message.from_user.id))

@router.message(F.text == "Оставить заявку")
async def start_form(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(Form.name)

@router.message(Form.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш номер телефона:")
    await state.set_state(Form.phone_number)

@router.message(Form.phone_number)
async def get_phone(message: types.Message, state: FSMContext):
    number = message.text.strip()
    if not number.isdigit() or len(number) < 10 or len(number) > 15:
        await message.answer("Пожалуйста, введите номер только цифрами. Пример: 8700123456")
        return
    await state.update_data(phone_number=number)
    await message.answer("Опишите вашу проблему:")
    await state.set_state(Form.support)

@router.message(Form.support)
async def get_support(message: types.Message, state: FSMContext):
    await state.update_data(support=message.text)
    data = await state.get_data()
    await save_application(
        user_id=message.from_user.id,
        name=data['name'],
        phone_number=data['phone_number'],
        support=data['support']
    )
    await message.answer("Спасибо! Ваша заявка принята.\nМы свяжемся с вами в ближайшее время.")
    await state.clear()

@router.message(Command("cancel"))
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Действие отменено.")
