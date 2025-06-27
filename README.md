# Telegram Bot: Сбор заявок

Простой и масштабируемый Telegram-бот на Python + aiogram 3 для сбора заявок от пользователей.

## Возможности

- Сбор заявок от пользователей через пошаговую форму (FSM)
- Проверка номера телефона
- Сохранение данных в SQLite с указанием времени
- Админ-панель с просмотром всех заявок
- Разделение логики для пользователей и админов
- Поддержка нескольких администраторов

## Структура проекта

project/
├── bot/
│ ├── main.py
│ ├── config.py
│ ├── database/db.py
│ ├── states/form.py
│ ├── keyboards/reply.py
│ ├── handlers/
│ │ ├── user.py
│ │ └── admin.py
├── requirements.txt
├── README.md
└── data.db (создаётся автоматически)

## Установка и запуск

1. Клонируй проект:
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
Установи зависимости:
    pip install -r requirements.txt

Добавь токен и список админов в bot/config.py:
    BOT_TOKEN = "ваш_токен"
    ADMIN_IDS = [123456789]

Запусти бота:
    python -m bot.main
## Тестовые команды
    Команда	Описание
    /start - Запуск бота
    Оставить заявку	Заполнение формы
    /cancel	- Отмена заявки
    Заявки	Только для админов (скрытая)

## Технологии
    Python 3.10+
    aiogram 3.x
    SQLite (через aiosqlite)
