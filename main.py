import newbot as keys
from telegram.ext import*
import response as r

print("Bot started...")


def start_command(update, context):
    update.mesage.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('Need any help! Ask it on Google')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

