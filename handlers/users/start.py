from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from keyboards.inline.menu_keyboard import menu  
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo(
        photo="https://i.pinimg.com/originals/f1/91/d3/f191d302eb21ade7ece59e9b209a4744.png",  # shu yerga rasm URL
        caption=f"<b>Salom, {message.from_user.full_name}!</b>",
        reply_markup=menu,
        parse_mode="HTML"
    )





