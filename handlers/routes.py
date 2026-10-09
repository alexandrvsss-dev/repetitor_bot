from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards import goal, class_kb, signup_kb, smena_kb, reviews_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from states import DiagnosticForm

router = Router()

ADMIN_ID = 7117139107

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Здравствуйте! Я Карина Петихина, преподаватель русского языка 👋\n\nБольше 10 лет помогаю школьникам разобраться в русском языке, восполнить пробелы и подготовиться к экзаменам.\n\nЗанимаюсь онлайн со школьниками 5–9 классов.\n\nДавайте сначала определимся, с чем нужна помощь 👇", reply_markup=goal)


@router.callback_query(F.data=="goal_school")
async def school(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Хорошо! Тогда уточним класс ребёнка\n\nС учениками 5–8 классов мы восполняем пробелы, разбираем сложные темы и постепенно выстраиваем  базу по русскому языку.\n\nВ каком классе сейчас учится ребёнок?", reply_markup=class_kb)

@router.callback_query(F.data=="goal_ag")
async def goal_og(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Отлично!\n\nЯ готовлю к ОГЭ системно: мы не просто решаем варианты экзамена, а сначала закрываем пробелы, накопившиеся за 5–8 классы, а затем постепенно отрабатываем все части ОГЭ.\n\nРебята регулярно пишут изложения и сочинения, каждый месяц выполняют пробный экзамен, а родители получают от меня отчёт о результатах и успеваемости.\n\nНо прежде чем начать подготовку, я приглашаю ученика на бесплатную диагностику знаний.\n\nНа ней я смотрю текущий уровень, определяю сильные и слабые стороны и понимаю, с какой точки нам нужно начинать подготовку.", reply_markup=signup_kb)


@router.callback_query(F.data.startswith("grade_"))
async def gradet(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    selected_grade = callback.data.split("_")[1]
    await state.update_data(grade=f"{selected_grade} класс")
    await callback.message.answer("Спасибо! Теперь я немного лучше понимаю Ваш запрос.\n\nПеред началом занятий я приглашаю каждого нового ученика на бесплатную диагностику знаний.\n\nЭто не контрольная и не экзамен 😊\n\nНа диагностике я знакомлюсь с ребёнком, смотрю, насколько уверенно он владеет основными темами, нахожу пробелы и понимаю, над чем нам нужно работать в первую очередь.\n\nПосле диагностики я расскажу Вам о результатах и предложу подходящий вариант занятий.", reply_markup=signup_kb)



@router.callback_query(F.data=="start_signup")
async def sign(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(DiagnosticForm.smena)
    await callback.message.answer("Отлично! Осталось несколько вопросов, чтобы я могла предложить Вам удобное время.\n\nВ какую смену учится ребёнок?", reply_markup=smena_kb)


@router.callback_query(F.data.startswith("shift_"))
async def shifting(callback: CallbackQuery, state:FSMContext):
    await callback.answer()
    selected_shifting = callback.data.split("_")[1]
    await state.update_data(shift=f"{selected_shifting} смена")
    await state.set_state(DiagnosticForm.chasovoy_poyas)
    await callback.message.answer("И ещё один важный момент 😊\n\nЯ работаю с учениками из разных городов, поэтому напишите, пожалуйста, Ваш город или разницу во времени с Москвой.\n\nНапример:\n\nМосква\nКалининград, −1 час от Москвы\nЕкатеринбург, +2 часа от Москвы")

@router.message(DiagnosticForm.chasovoy_poyas)
async def chas(message: Message, state: FSMContext):
    await state.update_data(chasovoy_poyas = message.text)
    data = await state.get_data()
    admin_text = f"""🔔 **НОВАЯ ЗАЯВКА НА ДИАГНОСТИКУ!**

👤 Пользователь: @{message.from_user.username} ({message.from_user.full_name})
📚 Класс: {data.get('grade', 'Не указано')}
⏰ Смена обучения: {data.get('shift', 'Не указано')}
🌍 Часовой пояс: {data.get('chasovoy_poyas', 'Не указано')}"""

    await message.bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="Markdown")
    await message.answer("Спасибо! Я получила Вашу заявку 🤎\n\nПодберу несколько подходящих вариантов времени для диагностики и напишу Вам лично.\n\nА пока можно немного познакомиться со мной и моей работой.\n\nНиже оставлю несколько отзывов родителей и учеников 👇")
    
    reviews_text = "⭐️ Отзыв 1 (ОГЭ, 9 класс):\n\nЗдравствуйте, у меня 37/37 за ОГЭ!\n Спасибо вам огромное за подготовку ❤️\nЭто был самый сложный предмет из всех ОГЭ для меня, я в шоке, что теперь такой балл\n\n\n⭐️ Отзыв 2 (ОГЭ, 9 класс):\n\nДобрый день. Хочу поблагодарить Вас за успешную подготовку моего ребёнка к ОГЭ по русскому! До этого каждое изложение и сочинение были трудным испытанием, но благодаря Вам дочь смогла с легкостью выполнять эти задания.\nТакже ребёнок стал разбираться в грамматике, синтаксисом.\nТакже хочу поблагодарить за доступную обратную связь.\nОчень у Вас понравилось, что занятия проводились без переносов, а ближе к дате экзамена была возможность взять дополнительные занятия.\nРезультат от занятий превзошел наши ожидания по усвоению материала за коротки срок (за полгода)\n\n\n⭐️ Отзыв 3 (ОГЭ, 9 класс):\n\nДоброй ночи, извините что поздно. Спасибо вам огромное, вы прям такая молодец я восхищаюсь 🤗 Гриша, сдал экзамен, до 5 не хватило 2 балла! Я в шоке, если бы не вы, мы бы точно не сдали."
    await message.answer(reviews_text)
    await message.answer("Это только небольшая часть отзывов.\n\nБольше результатов и впечатлений учеников и родителей я собрала в отдельном канале.", reply_markup=reviews_kb)
    await message.answer("Готово 🤎\n\nВаша заявка на бесплатную диагностику у меня.\n\nЯ посмотрю информацию и лично напишу Вам, чтобы подобрать удобное время.\n\nДо встречи!")
    await state.clear()
    