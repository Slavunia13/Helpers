from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonRequestChat

from aiogram.enums import ParseMode

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    kb = [
        [KeyboardButton(text="Записаться на консультацию")],
        [KeyboardButton(text="Контактная информация")],
        [KeyboardButton(text="Задать свой вопрос")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )

    await message.answer(
        "Вы довольны своей работой?", reply_markup=keyboard
    )



@router.message(F.text.startswith("Контактная информация"))
async def without_pureye(message: Message):
    await message.answer("*Номер телефона оператора:* номер телефона\n*Мы находимся здесь:* адрес \n*Рабочее время:* время работы \n", parse_mode=ParseMode.MARKDOWN_V2)


