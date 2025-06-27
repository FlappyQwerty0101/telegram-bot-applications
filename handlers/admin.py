from aiogram import Router, types, F

from config import ADMIN_IDS
from database.db import get_all_applications

router = Router()

@router.message(F.text == "Заявки")
async def view_applications(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return

    rows = await get_all_applications()
    if not rows:
        await message.answer("Пока нет заявок")
        return

    for row in rows:
        await message.answer(
            f"📋 Заявка #{row[0]}\n"
            f"👤 Имя: {row[1]}\n"
            f"📞 Телефон: {row[2]}\n"
            f"📝 Описание: {row[3]}\n"
            f"🕓 Время: {row[4]}"
        )