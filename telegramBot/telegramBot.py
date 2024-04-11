# from imaplib import Commands
# import os
# import telegramBot

# API_KEY=os.getenv('API_KEY')
# bot = telegramBot.telegramBot(API_KEY)
# @bot.message_handler(Commands=['Greet'])
# def greet(message):
#     bot.reply_to(message, 'Hey! Whats up bro?')
    
# bot.polling()



































# from email.headerregistry import MessageIDHeader
# from typing import Final
# from urllib import response

# from telegram import Update
# from telegram.ext import Application, CommandHandler,  ContextTypes

# TOKEN: Final = '7004939873:AAG2vPh9WkILSM1KiNzPjVNcdaXJwUtbaA8'
# BOT_USERNAME: Final = 'meebeg_bot'

# #Commands
# async def start_command(update: Update, context: ContentTypeHeader.DEFAULT_TYPE):
#     await update.message.reply_text('Hey!Thanks for chatting with me! My name is Banana!')
    
# async def help_command(update: Update, context: ContentTypeHeader.DEFAULT_TYPE):
#     await update.message.reply_text('I am Banana! How can I help you?') 
    
# async def custom_command(update: Update, context: ContentTypeHeader.DEFAULT_TYPE):
#     await update.message.reply_text('Send me a picture and wait for the emojis!!!!!!!!!!!!!!') 
    
# #Responses
# def handle_response(text: str) -> str:
#     processed = text.lower()

#     if 'hello' in processed:
#         return 'Hey there!'

#     elif 'whats up' in processed or 'how are you' in processed:
#         return 'I am okay, what about you?'

#     elif 'i am ok too' in processed or 'good' in processed:
#         return 'You\'re welcome ;)'

#     elif 'thank you' in processed or 'thanks' in processed:
#         return 'You\'re welcome'

#     else:
#         return 'I am sorry, I didn\'t understand that.'
#     return 'I dont understand what u wrote.....'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     if message_type == 'group':
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#         else:
#             response: str = handle_response(text)

    
#     print('Bot:', response)
#     await update.message.reply_text(response)
    
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f'Update {update} caused error {context.error}')
    
# if __name__ == '__main__':
#     print('Starting Banana.........')
#     app = Application.builder().token(TOKEN).build()
    



# app.add_handler(CommandHandler('start', start_command))
# app.add_handler(CommandHandler('custom', custom_command))
# app.add_handler(CommandHandler('help', help_command))

# #Messages
# app.add_handler(MessageHandler(filters.TEXT, handle_message))
# #Error
# app.add_error_handler(error)
# #Polls
# print('Polling......')
# app.run_polling(poll_interval = 5)
         
    

    
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.utils import executor

# TOKEN = '7004939873:AAG2vPh9WkILSM1KiNzPjVNcdaXJwUtbaA8'
# BOT_USERNAME = 'meebeg_bot'

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())

# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.reply('Hey! Thanks for chatting with me! My name is Banana!')

# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     await message.reply('I am Banana! How can I help you?')

# @dp.message_handler(commands=['custom'])
# async def custom_command(message: types.Message):
#     await message.reply('Send me a picture and wait for the emojis!')

# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def handle_message(message: types.Message):
#     text = message.text.lower()
#     if BOT_USERNAME in text:
#         text = text.replace(BOT_USERNAME, '').strip()

#     response = handle_response(text)
#     print('Bot:', response)
#     await message.reply(response)

# def handle_response(text: str) -> str:
#     processed = text.lower()

#     if 'hello' in processed:
#         return 'Hey there!'
#     elif 'whats up' in processed or 'how are you' in processed:
#         return 'I am okay, what about you?'
#     elif 'i am ok too' in processed or 'good' in processed:
#         return 'You\'re welcome ;)'
#     elif 'thank you' in processed or 'thanks' in processed:
#         return 'You\'re welcome'
#     else:
#         return 'I am sorry, I didn\'t understand that.'

# @dp.errors_handler()
# async def error(update, error):
#     print(f'Update {update} caused error {error}')

# if __name__ == '__main__':
#     print('Starting Banana...')
#     executor.start_polling(dp, skip_updates=True)
import telepot
from telepot.loop import MessageLoop

TOKEN = '7004939873:AAG2vPh9WkILSM1KiNzPjVNcdaXJwUtbaA8'
BOT_USERNAME = 'meebeg_bot'

#Commands
async def start_command(chat_id):
    bot.sendMessage(chat_id, 'Hey! Thanks for chatting with me! My name is Banana!')

async def help_command(chat_id):
    bot.sendMessage(chat_id, 'I am Banana! How can I help you?')

async def custom_command(chat_id):
    bot.sendMessage(chat_id, 'Send me a picture and wait for the emojis!')

#Responses
def handle_response(text: str) -> str:
    processed = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    elif 'whats up' in processed or 'how are you' in processed:
        return 'I am okay, what about you?'
    elif 'i am ok too' in processed or 'good' in processed:
        return 'You\'re welcome ;)'
    elif 'thank you' in processed or 'thanks' in processed:
        return 'You\'re welcome'
    else:
        return 'I am sorry, I didn\'t understand that.'

def handle_message(msg):
    chat_id = msg['chat']['id']
    message_type = msg['chat']['type']
    text = msg['text']

    print(f'User ({chat_id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            response = handle_response(text)

    print('Bot:', response)
    bot.sendMessage(chat_id, response)

def error(msg):
    print(f'Update {msg} caused an error.')

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    print('Starting Banana...')

    # Start message loop
    MessageLoop(bot, {'chat': handle_message,
                      'error': error}).run_as_thread()

    # Run forever
    while True:
        pass
