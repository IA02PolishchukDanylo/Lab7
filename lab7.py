from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lab7 EFK")
def log_message(update, context):
    message = update.message.text
    chat_id = update.effective_chat.id

    doc = {
        'message': message,
        'chat_id': chat_id
    }
    es.index(index='telegram_logs', doc_type='_doc', body=doc)

def error(update, context):
    print(f"Помилка: {context.error}")
def main():
    token = ''
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text,log_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

