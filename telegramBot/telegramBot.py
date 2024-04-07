from typing import Final
import telegram
from telegram import Update
from telegram.txt import Application, CommandFandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '7004939873:AAG2vPh9WkILSM1KiNzPjVNcdaXJwUtbaA8'
BOT_USERNAME: Final = 'meebeg_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hey!Thanks for chatting with me! My name is Banana!')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Banana! How can I help you?') 
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a picture and wait for the emojis!!!!!!!!!!!!!!') 
    
#Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
if 'hello' in processed:
    return 'Hey there!'

if 'whats up' or 'how are you' in processed:
    return 'M ok, what about u?'

if 'I am ok too' or 'Good' in processed:
    return 'Your welcome ;)'
if 'Thank you' or 'Thanks' in processed:
    return 'Nice to meet you!'
