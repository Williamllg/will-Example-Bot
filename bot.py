from pip import main
from telegram.ext import Updater , CommandHandler 

# Agregano un Handler que no es  mas que las acciones que le van entrando las demas personas 

def start(update , context):

    update.message.reply_text("Hola Humano")

if __name__== '__main__':
    updater = Updater(token='tu_token', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start" , start))
    # Agregando un Handler de Comando 

    # Esto es para que el bot se quede escuchando las ordenes que le van entranado por los parametros 
    updater.start_polling()
    updater.idle()
