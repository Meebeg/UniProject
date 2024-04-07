from email.headerregistry import ContentTypeHeader
from typing import Final
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update

TOKEN: Final = '7004939873:AAG2vPh9WkILSM1KiNzPjVNcdaXJwUtbaA8'
BOT_USERNAME: Final = 'meebeg_bot'

#Commands
async def start_command(update: Update, context: ContentTypeHeader.DEFAULT_TYPE):
    await update.message.reply_text('Hey!Thanks for chatting with me! My name is Banana!')
    
async def help_command(update: Update, context: ContentTypeHeader.DEFAULT_TYPE):
    await update.message.reply_text('I am Banana! How can I help you?') 
    
async def custom_command(update: Update, context: ContentTypeHeader.DEFAULT_TYPE):
    await update.message.reply_text('Send me a picture and wait for the emojis!!!!!!!!!!!!!!') 
    
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

