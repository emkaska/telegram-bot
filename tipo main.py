# import re
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, replymarkup
# from telegram.callbackquery import CallbackQuery
# from telegram.ext import (
#     CallbackContext,
#     Updater, 
#     updater,
#     CommandHandler, 
#     PicklePersistence,
#     Filters,
#     MessageHandler,
#     CallbackQueryHandler
# )
# from menu import main_menu_keyboard, info_menu_keyboard
# from credentials import TOKEN
# from key_buttons import leagues_buttons, info_menu
# from message import tablica


# def start(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Добро пожаловать👋, {username}, выберите турнир⚽️".format
#         (
#             username=update.effective_user.first_name \
#                 if update.effective_user.first_name is not None \
#                 else update.effective_user.username
#         ),
#         reply_markup=main_menu_keyboard()
#     )


# LEAGUES_REGEX = r"(?=(" + (leagues_buttons[0]) + r"))"
# BACK_REGEX = r"(?=(" + (info_menu[3]) + r"))"
# # UCL_REGEX = r"(?=(" + (info_menu[0]) + r"))"


# def receive_league_menu(update: Update, context: CallbackContext):
#     info = re.match(LEAGUES_REGEX, update.message.text)
#     update.message.reply_text(
#         "Выберите опцию🧾",
#         reply_markup=info_menu_keyboard()
#     )

# def back_league_menu(update: Update, context: CallbackContext):
#     info = re.match(BACK_REGEX, update.message.text)
#     update.message.reply_text(
#         "Выберите турнир⚽️",
#         reply_markup=main_menu_keyboard()
#     )

# def receive_info_menu(update: Updater, context: CallbackContext):
#     info = re.match(UCL_REGEX, update.message.text)
#     update.message.reply_text(
#         "Выберите опцию",
#         reply_markup=info_menu_keyboard()
#     )

# def ucl_inline_menu(update: Update, context: CallbackContext):
#     info = re.match(UCL_REGEX, update.message.text)
#     keyboard = [
#         [InlineKeyboardButton("Gg", callback_data='gg')],
#         [InlineKeyboardButton("Bb", callback_data='bb')],
#         [InlineKeyboardButton("Dd", callback_data='dd')],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text(
#         'Выберите опцию',
#         reply_markup=reply_markup
#     )

# def inline_buttons(update: Update, context: CallbackContext):
#     query = update.callback_query
#     query.answer()
#     if query.data == 'gg':
#         query.edit_message_text(
#             text="""
# # 1. Ливерпуль
# # 2. Челси
# # 3. Ман Сити
# # 4.
# # 5.           
# # """
#         )
#     if query.data == 'bb':
#         query.edit_message_text(
#             text="""
# 1. М.Салах   10
# 2. Ж.Варди   8
# 3. Р.Лукаку   5
# 4.
# 5.
# """
#         )
#     if query.data == 'dd':
#         query.edit_message_text(
#             text="""
# 1. Ф.Бруно    7
# 2. П.Погба   6
# 3. К.Д.Бройнэ   6
# 4.
# 5.
# """
#         )


# updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
# updater.dispatcher.add_handler(CommandHandler('start', start))

# updater.dispatcher.add_handler(MessageHandler(
#     Filters.regex(LEAGUES_REGEX),
#     receive_league_menu
#     ))

# updater.dispatcher.add_handler(MessageHandler(
#     Filters.regex(BACK_REGEX),
#     back_league_menu
#     ))

# updater.dispatcher.add_handler(MessageHandler(
#     Filters.regex(UCL_REGEX),
#     ucl_inline_menu
#     ))

# updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))


# updater.start_polling()
# updater.idle()s