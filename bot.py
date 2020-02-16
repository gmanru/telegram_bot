from telegram import  Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, Filters, MessageHandler

"""
/////////ПРИНЦИП РАБОТЫ БОТА С ТЕЛЕГОЙ///////////технология polling
БОТ -   -   -   -   -  СЕРВАК ТЕЛЕГИ

БОТ ->->есть инфа? ->-> СЕРВАК ТЕЛЕГИ
БОТ--<-<-нет инфы!-<-<- СЕРВАК ТЕЛЕГИ 

БОТ ->->есть инфа? ->-> СЕРВАК ТЕЛЕГИ
БОТ-<-Да,братан, лови в Update!-<-СЕРВАК ТЕЛЕГИ              

БОТ ->->есть инфа? ->-> СЕРВАК ТЕЛЕГИ
БОТ--<-<-нет инфы!-<-<- СЕРВАК ТЕЛЕГИ 

"""

button_help = 'Помощь'  #значение в кнопке

def button_help_handler(update: Update, context: CallbackContext):# update - ходит в телегу за обновлениями, качает все данные!!!     
    update.message.reply_text(                                      #context -  пользовательский контекст, пришедий от обработчика, можем сохранять пользовательские состояния
        text ='Help',
        reply_markup=ReplyKeyboardRemove(), #удаляем клаву
    )

def message_handler(update: Update, context: CallbackContext):   #обработчик
    text = update.message.text # из аргумента update достаем текст сообщения
    if text == button_help: #если полученный текст равен тексту в кнопке ЗНАЧИТ КНОПКУ ПРОЖАЛИ
        return button_help_handler(update=update, context=context) #вызываем функцию при прожатии кнопки


    reply_markup = ReplyKeyboardMarkup( #создаем клаву
        keyboard=[  #принимает список списков, вертикальные ряды //вроде так же и в вк
            [
            KeyboardButton(text=button_help)#кнопки по горизонтали
            ]
        ],
        resize_keyboard=True, #если поменяем кнопки, перерисуте под подходящий размер
    )
    
    
    update.message.reply_text(
        text ='Нажми на кнопку',
        reply_markup=reply_markup, #клава в таком натурном виде выводится
    )







def main(): 
    print('start')
    updater = Updater(
        token = 'ччч',  #токен бота 
        base_url="https://telegg.ru/orig/bot",  #прокси
        use_context=True,   #прописывать надо для либо 12 версии
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling() # запускает скачивание обновлений с сервака телеги один раз
    updater.idle() # позволяет застыть коду до тех пор пока не отрубим его сами
    print('finish')

if __name__ == '__main__':  # для запуска программы
    main()   