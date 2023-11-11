from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from datetime import datetime, timedelta

from random import randint
import calendar

router = Router()

MONTH = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
current_date = {}


def get_next_month(current_date) -> datetime:
    if current_date.month == 12:
        return current_date.replace(month=1, year=current_date.year + 1, day=1)

    return current_date.replace(month=current_date.month + 1, day=1)

def get_previous_month(current_date) -> datetime:
    if current_date.month == 1:
        return current_date.replace(month=12, year=current_date.year - 1, day=1)
    
    return current_date.replace(month=current_date.month - 1, day=1)
    

def get_text_data(current_date):    
    _, cnt_day = calendar.monthrange(2023, current_date.month)

    builder = InlineKeyboardBuilder()
    keyboard = [[InlineKeyboardButton(text=MONTH[current_date.month - 1] + ' ' + str(current_date.year), callback_data="iop")]]

    for i in range(cnt_day):
        if i // 7 + 1 >= len(keyboard):
            keyboard.append([])
        keyboard[i // 7 + 1].append(InlineKeyboardButton(text=str(i + 1), callback_data="booking_day"))

    while len(keyboard[-1]) < 7:
        keyboard[-1].append(InlineKeyboardButton(text=" ", callback_data="iop"))

    keyboard.append([])
    keyboard[-1].append(InlineKeyboardButton(text="<-", callback_data="prev_month"))
    keyboard[-1].append(InlineKeyboardButton(text="->", callback_data="next_month"))

    return {"buttons": InlineKeyboardMarkup(inline_keyboard=keyboard)}

def get_hour_data():    
    keyboard = [[InlineKeyboardButton(text="Выберите время консультации:", callback_data="iop", col_width=7)]]
    keyboard.append([])
    keyboard.append([])
    for i in range(8):
        keyboard[i // 4 + 1].append(InlineKeyboardButton(text=str(i + 11) + ":00", callback_data="booking_hour"))

    return {"buttons": InlineKeyboardMarkup(inline_keyboard=keyboard)}

@router.message(F.text.startswith("Записаться на консультацию"))
async def booking(message: Message):

    current_date[message.from_user.id] = datetime.now()
    text_data = get_text_data(current_date[message.from_user.id])

    await message.answer("Выберите дату консультации:", reply_markup=text_data["buttons"])

@router.callback_query(F.data == "next_month")
async def next_month(callback: CallbackQuery):
    global current_date
    current_date[callback.from_user.id] = get_next_month(current_date[callback.from_user.id])
    
    text_data = get_text_data(current_date[callback.from_user.id])
    
    await callback.message.edit_text("Выберите дату консультации:", reply_markup=text_data["buttons"])

@router.callback_query(F.data == "prev_month")
async def prev_month(callback: CallbackQuery):
    global current_date
    current_date[callback.from_user.id] = get_previous_month(current_date[callback.from_user.id])

    text_data = get_text_data(current_date[callback.from_user.id])
    
    await callback.message.edit_text("Выберите дату консультации:", reply_markup=text_data["buttons"])


@router.callback_query(F.data == "booking_day")
async def day_number(callback: CallbackQuery):
    text_data = get_hour_data()

    await callback.message.edit_text("Выберите дату консультации:", reply_markup= text_data["buttons"])

@router.callback_query(F.data == "booking_hour")
async def day_number(callback: CallbackQuery):
    text_data = get_hour_data()

    await callback.message.edit_text("Вы успешно записались на 13:00 15-го ноября.")