import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import BadRequest
import time
import telegram
from arkserverstats import *
from config import *


def is_admin(update):  # checks whether user is admin
    if (update.effective_user.id in ALL_ADMINS):
        return True


def unknown(update, context):
    if is_admin(update):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry i don't know this command")


def unauthorized(update, context):
    if is_admin(update):
        context.bot.send_message(chat_id=update.effective_user.id,
                                 text='You are authorized')
    else:
        context.bot.send_message(chat_id=update.effective_user.id,
                                 text='You are not authorized')

def start(update, context):  
    if is_admin(update):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="You are authorized, have fun!")
    else:
        context.bot.send_message(chat_id=update.effective_user.id,
                                 text='You are not authorized to use this bot.')


def all_stats(update, context):
    data = LostA_servers.get_server_list_status()["data"].items()
    s = ""
    for k,v in data:
        s += k + ": " + v + "\n"
    context.bot.send_message(chat_id=TARGET_GROUP,
                                            text=("Here is a overview of all Servers: " + "\n" + s.strip()))


# TODO: Input fo entering specific server + Change to english text
def stats(update, context): 
    server_stats = (LostA_servers.get_server_status("Slen")["data"]["Slen"])
    if "Ok" in server_stats:
        context.bot.send_message(chat_id=TARGET_GROUP,
                                     text="Slen Server Status ist: " + server_stats + "\n" + "Auf geht's, rein in die Masse!"+ "\U0001F604")
    elif "Busy" in server_stats:
        context.bot.send_message(chat_id=TARGET_GROUP,
                                        text="Slen Server Status ist: " + server_stats + "\n" + "Jetzt aber schnell rein in die Olga!" + "\U0001F632")
    elif "Full" in server_stats:
        context.bot.send_message(chat_id=TARGET_GROUP,
                                        text="Slen Server Status ist: " + server_stats + "\n" + "Oh, oh...das könnte Ewigkeiten dauern" + "\U0001F635")



updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Command Handler
start_handler = CommandHandler('start', start)

all_stats_handler = CommandHandler('all_stats', all_stats)
stats_handler = CommandHandler('stats', stats)

help_handler = CommandHandler('help', help)

unauthorized_handler = CommandHandler('unauthorized', unauthorized)
unknown_handler = MessageHandler(Filters.command, unknown)



# Dispatcher add CommandHandler
dispatcher.add_handler(start_handler)
dispatcher.add_handler(all_stats_handler)
dispatcher.add_handler(stats_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(unauthorized_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
