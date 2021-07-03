import logging
import pytz
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from datetime import time, tzinfo, timezone, datetime
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, JobQueue, MessageHandler,  Filters
from Unibz import getlecture

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

choices = []

links = []

def start(update: Update, _: CallbackContext) -> None:
  choices.clear()
  keyboard = [
        [
            InlineKeyboardButton("Scienze informatiche", callback_data='22'),
            InlineKeyboardButton("Economia", callback_data='26'),
        ],
        [InlineKeyboardButton("Scienze della formazione", callback_data='27'),
        InlineKeyboardButton("Design e arti", callback_data="44")],
        [InlineKeyboardButton("Scienze e tecnologie", callback_data="370")]
    ]

  reply_markup = InlineKeyboardMarkup(keyboard)

  update.message.reply_text('choose a department:', reply_markup=reply_markup)

def scienzeinformatiche(bot, update):
    choices.append("22")
    bot.callback_query.message.edit_text(scienzeinformatiche_message(),
                          reply_markup=scienzeinformatiche_keyboard())

def scienzeinformatiche_keyboard():
  keyboard = [[InlineKeyboardButton('Laurea in Informatica', callback_data='13441')],
              [InlineKeyboardButton('Informatica e Managemente delle aziende', callback_data='13371')],
              [InlineKeyboardButton('PhD in Computer Science', callback_data='13408')],
              [InlineKeyboardButton('Data Science Computazionale', callback_data='13447')],
              [InlineKeyboardButton('Magistrale interateneo Ingegneria del Software', callback_data='13398')],
              [InlineKeyboardButton("Scienze ed Ingegneria dell'informazione", callback_data='13322')],
              [InlineKeyboardButton('Software Engineering for Information System', callback_data='13422')]]
  return InlineKeyboardMarkup(keyboard)

def scienzeinformatiche_message():
  return 'Choose a course:'


def economia(bot, update):
    choices.append("26")
    bot.callback_query.message.edit_text(economia_message(),
                          reply_markup=economia_keyboard())

def economia_keyboard():
  keyboard = [[InlineKeyboardButton('PhD Management and Economics', callback_data='13274%2C13392')],
              [InlineKeyboardButton('Master in Hospitality Management', callback_data='13230')],
              [InlineKeyboardButton('Master imprenditorialità e Innovazione', callback_data='13373')],
              [InlineKeyboardButton('Tourism, Sport and Event Management', callback_data='13300%2C13418')],
              [InlineKeyboardButton('Politiche pubbliche ed Amministrazione', callback_data='13308%2C13426')],
              [InlineKeyboardButton("Scienze economiche e sociali", callback_data='13182%2C13324')],
              [InlineKeyboardButton('Accounting e Finanza', callback_data='13209%2C13445')],
              [InlineKeyboardButton("Economia e Management", callback_data='13181%2C13323')],
              [InlineKeyboardButton("Master Impreditorialità e Innovazione 2019/20 1° anno", callback_data='13309')],
              [InlineKeyboardButton("Magistrale Economia e Management del settore pubblico", callback_data='13178%2C13320')],
              [InlineKeyboardButton("Master Euregio in Amminstrazione Pubblica", callback_data='13213')],
              [InlineKeyboardButton("PhD Management and Economics on Organizational and Institutional Outliers", callback_data='13291%2C13409')],
              [InlineKeyboardButton("Gestione aziendale - Management del turismo", callback_data='13268')],
              [InlineKeyboardButton("Gestione Aziendale - Management Sport ed eventi", callback_data='13253')]]
  return InlineKeyboardMarkup(keyboard)

def economia_message():
  return 'Choose a course:'

def formazione(bot, update):
    choices.append("27")
    bot.callback_query.message.edit_text(formazione_message(),
                          reply_markup=formazione_keyboard())

def formazione_keyboard():
  keyboard = [[InlineKeyboardButton('Magistrale in Musicologia', callback_data='13397')],
              [InlineKeyboardButton('Servizio Sociale DM270', callback_data='13414')],
              [InlineKeyboardButton('Magistrale in Linguistica Applicata', callback_data='13421')],
              [InlineKeyboardButton('Educatore sociale DM270', callback_data='13380')],
              [InlineKeyboardButton('Scienze della comunicazione e cultura', callback_data='13335')],
              [InlineKeyboardButton("24 CFU in Lingua tedesca", callback_data='13444')],
              [InlineKeyboardButton('Quadriennale in Scienze della Formazione primaria - IT', callback_data='13376')],
              [InlineKeyboardButton("Magistrale in Innovazione e Ricerca per gli interventi socio-assistenziali-educativi - 1° anno", callback_data='13181')],
              [InlineKeyboardButton("Magistrale in Innovazione e Ricerca per gli interventi socio-assistenziali-educativi - 2° anno", callback_data='13411')],
              [InlineKeyboardButton("Formazione primaria - DE", callback_data='13327')],
              [InlineKeyboardButton("Formazione primaria - IT", callback_data='13190')],
              [InlineKeyboardButton("Formazione primaria - LAD", callback_data='13329')],
              [InlineKeyboardButton("Cultura ladina e Antropologia alpina ANTROPOLAD", callback_data='13307')],
              [InlineKeyboardButton("Quadriennale in scienze della Formazione primaria - IT", callback_data='13360')],
              [InlineKeyboardButton("Dottorato in Pedagogia generale, sociale e didattica generale e disciplinare", callback_data='13394')],
              [InlineKeyboardButton("Idoneità destinato a insegnati di italiano della PA Bolzano", callback_data='13427')],
              [InlineKeyboardButton("Sostegno alunni con disabilità - sezione tedesca", callback_data='13459')],
              [InlineKeyboardButton("Sostegno alunni con disabilità - sezione italiana", callback_data='13388')],
              [InlineKeyboardButton("Formazione per insegnanti di sostengo in provincia di Bolzano", callback_data='13388')]]
  return InlineKeyboardMarkup(keyboard)

def formazione_message():
  return 'Choose a course:'


def designearti(bot, update):
    choices.append("44")
    bot.callback_query.message.edit_text(designearti_message(),
                          reply_markup=designearti_keyboard())

def designearti_keyboard():
  keyboard = [[InlineKeyboardButton('Master design per bambini', callback_data='13460')],
              [InlineKeyboardButton('Magistrale in Design eco-sociale', callback_data='13240%2C13352')],
              [InlineKeyboardButton('laurea in design e arti - curriculum Arte', callback_data='13241%2C13353')],
              [InlineKeyboardButton('laurea in design e arti - curriculum Design', callback_data='13267%2C13385')]]
  return InlineKeyboardMarkup(keyboard)

def designearti_message():
  return 'Choose a course:'


def scienzeetecnologie(bot, update):
    choices.append("370")
    bot.callback_query.message.edit_text(scienzeetecnologie_message(),
                          reply_markup=scienzeetecnologie_keyboard())

def scienzeetecnologie_keyboard():
  keyboard = [[InlineKeyboardButton('Lauree FaST', callback_data='13216')],
              [InlineKeyboardButton('Ingegneria del legno', callback_data='13273%2C13391')],
              [InlineKeyboardButton('PhD Advanced Systems Engineering ASE', callback_data='13315%2C13424')],
              [InlineKeyboardButton('Precorso di Matematica', callback_data='13388')],
              [InlineKeyboardButton('PhD Food Engineering and Biotechnology', callback_data='13206%2C13442')],
              [InlineKeyboardButton('Magistrale in Ingegneria Energetica', callback_data='13224%2C13336')],
              [InlineKeyboardButton('PhD Sustainable Energy and Technologies SET', callback_data='13188%2C13330')],
              [InlineKeyboardButton('PhD Mountain Environment and Agriculture MEA', callback_data='13252%2C13364')],
              [InlineKeyboardButton('ADMISSION TEST Faculty of Science and Technology', callback_data='13215%2C13451')],
              [InlineKeyboardButton('Magistrale in Ingegneria Industriale Meccanica', callback_data='13278%2C13396')],
              [InlineKeyboardButton('Master in Viticulture, enology and wine management', callback_data='13217%2C13453')],
              [InlineKeyboardButton("Scienze Agrarie, degli Alimenti e dell'Ambiente Montano", callback_data='13310%2C13420')],
              [InlineKeyboardButton('Ingegneria Industriale Meccanica', callback_data='13189%2C13331')],
              [InlineKeyboardButton('Scienze Agrarie e Agroalimentari', callback_data='13227%2C13339')],
              [InlineKeyboardButton("Magistrale internazionale in Gestione sostenibile dell'ambiente montano", callback_data='13192%2C13428')],
              [InlineKeyboardButton('Food Sciences for Innovation and Authenticity', callback_data='13210%2C13446')],
              [InlineKeyboardButton('Ingegneria logistica e della produzione - fino 2015', callback_data='13261%2C13379')],
              [InlineKeyboardButton('Magistrale internazione in Ortofrutticoltura', callback_data='13288%2C13406')],
              [InlineKeyboardButton("Master Hyrma", callback_data='13448')]]
  return InlineKeyboardMarkup(keyboard)

def scienzeetecnologie_message():
  return 'Choose a course:'

def alarm(context: CallbackContext) -> None:
    """Send the alarm message."""
    job = context.job
    
    lectures, time = getlecture(choices[0], choices[1])

    rep = "I found this lectures: \n"
    for i in range(len(lectures)):
        rep = rep + lectures[i] + " at " + time[i] + "\n"
    context.bot.send_message(job.context, text=rep)

def set_timer(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    d = datetime.now()
    timezone = pytz.timezone("Europe/Rome")
    d_aware = timezone.localize(d)
    text = update.message.text
    text = text.replace("/notif","")
    temp = text.split(":")
    hour = temp[0]
    hour = int(hour)
    mins = temp[1]
    mins = int(mins)
    notify_time = time(hour, mins, 0, 0, tzinfo=d_aware.tzinfo)
    try:
        context.job_queue.run_daily(alarm,notify_time, context=chat_id, name=str(chat_id))

        text = 'Alarm successfully set! use /stop command to delete it'
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

def stop_timer(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.message.chat_id, text='Stoped!')
    context.job_queue.stop()


def button(update: Update, _: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    choice = query.data
    choices.append(choice)
    lectures, time = getlecture(choices[0], choices[1])

    rep = "I found this lectures: \n"
    for i in range(len(lectures)):
        rep = rep + lectures[i] + " at " + time[i] + "\n"
    rep = rep + "use /notif hour:mins to set the alarm daily"
    query.edit_message_text(text=rep)


def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot. Use /info to know who coded this bot.")

def info(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("This bot was created by Diego Loiacono. Github link: https://github.com/diegoloiac")


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('notif', set_timer, pass_job_queue=True))
    updater.dispatcher.add_handler(CommandHandler('stop', stop_timer, pass_job_queue=True))
    updater.dispatcher.add_handler(CallbackQueryHandler(scienzeinformatiche, pattern='22'))
    updater.dispatcher.add_handler(CallbackQueryHandler(economia, pattern='26'))
    updater.dispatcher.add_handler(CallbackQueryHandler(formazione, pattern='27'))
    updater.dispatcher.add_handler(CallbackQueryHandler(designearti, pattern='44'))
    updater.dispatcher.add_handler(CallbackQueryHandler(scienzeetecnologie, pattern='370'))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('info', info))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()