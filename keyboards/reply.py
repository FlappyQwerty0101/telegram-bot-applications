from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from config import ADMIN_IDS

def support_keyboard(user_id: int):
    buttons = [[KeyboardButton(text="Оставить заявку")]]
    if user_id in ADMIN_IDS:
        buttons.append([KeyboardButton(text="Заявки")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)