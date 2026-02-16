from telegram.ext import Updater, CommandHandler
from telegram import BotCommand

import handlers
import settings

def main():
    bot = Updater(settings.API_TOKEN)
    dp = bot.dispatcher
    bot.bot.set_my_commands([
        BotCommand("/start", "Запускает бота"),
        BotCommand("/langs", "Выводит все языки программирования"),
        BotCommand("/city", "Выводит все города россии"),
        BotCommand("/countries", "Выводит все страны мира"),
        BotCommand("/names", "Выводит все имена"),
        BotCommand("/curse", "Выводит курс рубля к доллару"),
        BotCommand("/update", "Обновляет данные"),
    ])
    dp.add_handler(CommandHandler("start", handlers.greet_user))
    dp.add_handler(CommandHandler("langs", handlers.get_langs))
    dp.add_handler(CommandHandler("city", handlers.get_cities))
    dp.add_handler(CommandHandler("countries", handlers.get_countries))
    dp.add_handler(CommandHandler("names", handlers.get_names))
    dp.add_handler(CommandHandler("curse", handlers.get_curse))
    dp.add_handler(CommandHandler("update", handlers.save))
    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
