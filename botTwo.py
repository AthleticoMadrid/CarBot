import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, guess_number, send_car_picture, user_coordinates,
                        talk_to_me)
import settings

logging.basicConfig(filename='botTwo.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
        'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("car", send_car_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать фото автомобиля)$'), send_car_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот запустился")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()