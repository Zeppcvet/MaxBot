#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import urllib.request
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class BestChange:
    def __init__(self):

        self.url = 'https://www.bestchange.ru/privat24-uah-to-sberbank.html'

    def rate(self):

        html = urllib.request.urlopen(self.url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup.find_all('td', attrs={'class': 'bi'})
        result = tags[1].text.strip()
        return result
    def print_rate(self):
        if __name__ == "__main__":
          answer = BestChange()
          return answer.rate()


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = "secret"

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def reply(update, context):
    """Reply to the user message."""
    useranswer = BestChange()
    useranswer.rate()
    useranswer.print_rate()
    update.message.reply_text("Bestchange.ru |"+useranswer.print_rate() + "\nWebsite2.ru      | ПримерОтвета" + "\nWebsite3.ru      | ПримерОтвета" + "\nWebsite4.ru      | ПримерОтвета" +
                              "\nWebsite5.ru      | ПримерОтвета" + "\nWebsite6.ru      | ПримерОтвета" + "\nWebsite7.ru      | ПримерОтвета" + "\nWebsite8.ru      | ПримерОтвета" + "\nWebsite9.ru      | ПримерОтвета" + "\nWebsite10.ru    | ПримерОтвета")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, reply))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    main()