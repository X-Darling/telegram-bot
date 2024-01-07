from typing import Final
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters,  ContextTypes
TOKEN: Final =  '5869601561:AAFkCwg04fAxoMK-F9F2g3KO7C_DmRTaLtg'
BOT_USERNAME: Final = '@demo_test_c01_ep1_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello thanls for chatting  with us i am test subject')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('so you want help ok great')

async def gnu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please send general FSF & GNU inquiries to gnu@gnu.org There are also other ways to contact the FSF. Broken links and other corrections or suggestions can be sent to webmasters@gnu.org Please see the Translations README for information on coordinating and contributing translations of this article')

#reponses
def handle_response(text: str)->str:
    processed: str = text.lower()
    if 'hello' in processed:
        return "hii how are you man"
    if 'ping' in processed:
        return 'yes iam alive'
    if 'peter' in processed:
        return 'ohh i know peter, \n he is a creature with a girl font'
    return ''

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'(User{update.message.chat.id}in {message_type}: "{text}")')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            reponse = handle_response(new_text)
        else:
            return
    else:
        reponse: str = handle_response(text)
    print('Bot',reponse)
    await update.message.reply_text(reponse)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'{update}caused error {context.error}')


if __name__ == '__main__':
    print('starting...')

    app = Application.builder().token(TOKEN).build()
    #Command
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('gnu',gnu_command))

    #message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #error

    app.add_error_handler(error)
    print('polling...')
    app.run_polling(poll_interval=3)











