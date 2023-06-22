from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import sqlite3
from math import radians, cos, sin, asin, sqrt

conn = sqlite3.connect("./Parchi.db")
print("Opened database successfully");
"""
def Parchi_valeggio(): 
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM [Parchi e giardini_Valeggio]')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as sqlerror:
        print("Error while connecting to sqlite", sqlerror)
"""
def execute_query(query):
    conn = sqlite3.connect("Parchi.db")
    cursor = conn.execute(query)
    results = cursor.fetchall
    conn.close()
    return results
def format_results(results):
    formatted = ''
    for row in results(results):
        formatted += "Nomeidentificativo: {}, Indirizzo: {}, Mq: {}, Attrezzato: {}, Note: {}, Parcogiochi: {}, Campisportivi: {}, Zoneriposo: {}\n" .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    return formatted

def printparco(update,context):
    query= "SELECT * FROM [Parchi e girdini_Sona]"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco parchi Sona:\n" + formatted_results
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

printparco()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Benvenuto nel Servizio di ricerca dei parchi e giardini di Verona\nPer scegliere i filtri di riceca digita /filtri")
    

async def filtri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Scegli i filtri in base ai quali avverà la ricerca\n")
    

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def main() -> None:
    #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler('help', help))
    app.run_polling()

if __name__=='__main__':
   main()


