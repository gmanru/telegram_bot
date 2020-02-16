from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters

TG_TOKEN = 'ччч'

def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'anonymous'
    
    text = update.effective_message.text
    reply_text = f'Привет, {name}!\n\n{text}'

    bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = reply_text,
    )
    
    
    
    
    return



def main(): 
    print('start')
    bot = Bot(
        token = TG_TOKEN,
        base_url="https://telegg.ru/orig/bot",
    )
    updater = Updater(
        bot = bot,
    )

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
    print('finish')

if __name__ == '__main__':
    main()   
