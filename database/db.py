import aiosqlite

from datetime import datetime

from config import DB_NAME

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT,
                phone_number TEXT,
                support TEXT,
                created_at TEXT
            )
        """)
        await db.commit()

async def save_application(user_id: int, name: str, phone_number: str, support: str):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO applications (user_id, name, phone_number, support, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, name, phone_number, support, created_at))
        await db.commit()

async def get_all_applications():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("""
            SELECT id, name, phone_number, support, created_at
            FROM applications
            ORDER BY created_at DESC
        """)
        return await cursor.fetchall()