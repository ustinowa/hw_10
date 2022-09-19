from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackContext
import exprt
import impr


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello, hi {update.effective_user.first_name}')


def export_handler(update: Update, context: CallbackContext):
    a = update.message.text.split()
    print(a)
    if a[1] == '1':
        res = exprt.write_file_1()
        print(res)
        update.message.reply_text(f'{res}')
    if a[1] == '2':
        update.message.reply_text(f'{exprt.write_file_2()}')

def import_handler(update: Update, context: CallbackContext):
    a = update.message.text.split()
    if a[1] == '1':
        update.message.reply_text(f'{impr.read_file_1()}')
    if a[1] == '2':
        update.message.reply_text(f'{impr.read_file_2()}')
        
        
app = Updater('5779007061:AAFyygQyXSoq1dR2VMGN1q7m3NhHTOPwvLQ')
app.dispatcher.add_handler(CommandHandler("hello", hello))
app.dispatcher.add_handler(CommandHandler('export', export_handler))
app.dispatcher.add_handler(CommandHandler('import', import_handler))


app.start_polling()
app.idle()