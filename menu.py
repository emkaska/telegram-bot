import telegram 
from key_buttons import leagues_buttons 


def main_menu_keyboard():
    keyboard=([
        [
        telegram.KeyboardButton(leagues_buttons[0]),
        telegram.KeyboardButton(leagues_buttons[1]),
        ],

        [
        telegram.KeyboardButton(leagues_buttons[2]),
        telegram.KeyboardButton(leagues_buttons[3]),
        ],

        [
        telegram.KeyboardButton(leagues_buttons[4]),
        ],

        [
        telegram.KeyboardButton(leagues_buttons[5]),
        telegram.KeyboardButton(leagues_buttons[6]),
        ]

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

# def info_menu_keyboard():
#     keyboard=([
#         [
#         telegram.KeyboardButton(info_menu[0]),
#         telegram.KeyboardButton(info_menu[1]),
#         telegram.KeyboardButton(info_menu[2]),
#         ],

        # [
        # telegram.KeyboardButton(info_menu[3]),
        # ]

    # ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


