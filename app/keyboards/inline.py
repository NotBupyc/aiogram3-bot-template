from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def channels_not_sub(channels: list) -> InlineKeyboardMarkup:
    markup = []

    for i, channel in enumerate(channels, start=1):
        markup.append([
            InlineKeyboardButton(text=f'Канал #{i}', url=channel)
        ])

    else:
        markup.append([
            InlineKeyboardButton(text=f'Проверить подписку', callback_data="check_sub")
        ])

        return InlineKeyboardBuilder(markup=markup).as_markup()
