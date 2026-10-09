from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

goal = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подготовка к ОГЭ", callback_data="goal_ag")],
        [InlineKeyboardButton(text="Школьная программа", callback_data="goal_school")]
    ]
)

class_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="5 класс", callback_data="grade_5")],
        [InlineKeyboardButton(text="6 класс", callback_data="grade_6")],
        [InlineKeyboardButton(text="7 класс", callback_data="grade_7")],
        [InlineKeyboardButton(text="8 класс", callback_data="grade_8")]
    ]
)

signup_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Записаться на диагностику", callback_data="start_signup")]
    ]
)

smena_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Первая смена", callback_data="shift_1")],
        [InlineKeyboardButton(text="Вторая смена", callback_data="shift_2")]
    ]
)

reviews_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💬 Посмотреть все отзывы", url= "https://t.me/about_glagolpravilno")]
    ]
)