import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, replymarkup
from telegram.callbackquery import CallbackQuery
from telegram.ext import (
    CallbackContext,
    Updater, 
    updater,
    CommandHandler, 
    PicklePersistence,
    Filters,
    MessageHandler,
    CallbackQueryHandler
)
from telegram.files.document import Document
from menu import main_menu_keyboard
from credentials import TOKEN
from key_buttons import leagues_buttons
from take_screen import crop_image



def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Добро пожаловать👋, {username}, выберите турнир⚽️".format
        (
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )


LEAGUES1_REGEX = r"(?=(" + (leagues_buttons[0]) + r"))"
LEAGUES2_REGEX = r"(?=(" + (leagues_buttons[1]) + r"))"
LEAGUES3_REGEX = r"(?=(" + (leagues_buttons[2]) + r"))"
LEAGUES4_REGEX = r"(?=(" + (leagues_buttons[3]) + r"))"
LEAGUES5_REGEX = r"(?=(" + (leagues_buttons[4]) + r"))"
LEAGUES6_REGEX = r"(?=(" + (leagues_buttons[5]) + r"))"
LEAGUES7_REGEX = r"(?=(" + (leagues_buttons[6]) + r"))"


def receive1_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES1_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=ucl_inline_buttons()
    )

def receive2_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES2_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=uel_inline_buttons()
    )

def receive3_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES3_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=epl_inline_buttons()
    )

def receive4_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES4_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=l1_inline_buttons()
    )

def receive5_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES5_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=bl_inline_buttons()
    )

def receive6_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES6_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=sa_inline_buttons()
    )

def receive7_league_menu(update: Update, context: CallbackContext):
    info = re.match(LEAGUES7_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите опцию🧾",
        reply_markup=ll_inline_buttons()
    )


def ucl_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица ЛЧ⭐️", callback_data='Таблица ЛЧ⭐️')],
        [InlineKeyboardButton("Бомбардиры ЛЧ⚽️", callback_data='Бомбардиры ЛЧ⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def uel_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица ЛЕ💥", callback_data='Таблица ЛЕ💥')],
        [InlineKeyboardButton("Бомбардиры ЛЕ⚽️", callback_data='Бомбардиры ЛЕ⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def epl_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица АПЛ🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data='Таблица АПЛ🏴󠁧󠁢󠁥󠁮󠁧󠁿')],
        [InlineKeyboardButton("Бомбардиры АПЛ⚽️", callback_data='Бомбардиры АПЛ⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def l1_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица Лига1🇫🇷", callback_data='Таблица Лига1🇫🇷')],
        [InlineKeyboardButton("Бомбардиры Лига1⚽️", callback_data='Бомбардиры Лига1⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def bl_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица Бундес Лига🇩🇪", callback_data='Таблица Бундес Лига🇩🇪')],
        [InlineKeyboardButton("Бомбардиры Бундес Лига⚽️", callback_data='Бомбардиры Бундес Лига⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def sa_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица Серия А🇮🇹", callback_data='Таблица Серия А🇮🇹')],
        [InlineKeyboardButton("Бомбардиры Серия А⚽️", callback_data='Бомбардиры Серия А⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def ll_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Таблица Ла Лига🇪🇸", callback_data='Таблица Ла Лига🇪🇸')],
        [InlineKeyboardButton("Бомбардиры Ла Лига⚽️", callback_data='Бомбардиры Ла Лига⚽️')],
        
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def inline_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'Таблица ЛЧ⭐️':
        filename = crop_image('https://www.flashscore.ru/football/europe/champions-league/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры ЛЧ⚽️':
        filename = crop_image('https://www.sports.ru/ucl/bombardiers/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Таблица ЛЕ💥':
        filename = crop_image('https://www.flashscore.ru/football/europe/europa-league/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры ЛЕ⚽️':
        filename = crop_image('https://www.sports.ru/liga-europa/stat/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Таблица АПЛ🏴󠁧󠁢󠁥󠁮󠁧󠁿':
        filename = crop_image('https://www.flashscore.ru/football/england/premier-league/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры АПЛ⚽️':
        filename = crop_image('https://terrikon.com/football/england/championship/strikers')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Таблица Лига1🇫🇷':
        filename = crop_image('https://www.flashscore.ru/football/france/ligue-1/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры Лига1⚽️':
        filename = crop_image('https://www.sports.ru/ligue-1/stat/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Таблица Бундес Лига🇩🇪':
        filename = crop_image('https://www.flashscore.ru/football/germany/bundesliga/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры Бундес Лига⚽️':
        filename = crop_image('https://www.sports.ru/bundesliga/stat/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Таблица Серия А🇮🇹':
        filename = crop_image('https://www.flashscore.ru/football/italy/serie-a/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры Серия А⚽️':
        filename = crop_image('https://www.sports.ru/seria-a/stat/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Таблица Ла Лига🇪🇸':
        filename = crop_image('https://www.flashscore.ru/football/spain/laliga/standings/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )
    if query.data == 'Бомбардиры Ла Лига⚽️':
        filename = crop_image('https://www.sports.ru/la-liga/stat/')
        context.bot.sendDocument(
            update.effective_chat.id,
            document=open(filename, 'rb')
        )



updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES1_REGEX),
    receive1_league_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES2_REGEX),
    receive2_league_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES3_REGEX),
    receive3_league_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES4_REGEX),
    receive4_league_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES5_REGEX),
    receive5_league_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES6_REGEX),
    receive6_league_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LEAGUES7_REGEX),
    receive7_league_menu
    ))


updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))


updater.start_polling()
updater.idle()


