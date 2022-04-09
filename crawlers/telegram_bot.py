import logging

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

from constants import TELEGRAM_API_KEY
from repositories import utils_repository
from scrapper import crawler_reddit

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def nada_pra_fazer(update: Update, context: CallbackContext) -> None:
    """Call the crawler and returns the buzzer threads to telegram.

    Args:
        update (Update): The telegram update object.
        context (CallbackContext): The telegram callback context object.
    """
    subreddits = update.message.text.split()
    if len(subreddits) == 1:
        update.message.reply_text(
            "You don't informed me any subreddit. I will try /r/random, just a moment!"
        )
        subreddits = "random"
    else:
        subreddits = subreddits[1]
        update.message.reply_text(
            "Ok, I will search for the buzzer threads in those subreddits, just a moment!"
        )
    buzz_thread_list = crawler_reddit(subreddits)
    telegram_message_list = utils_repository.create_list_of_messages_to_telegram(
        buzz_thread_list
    )
    if len(telegram_message_list) == 0:
        update.message.reply_text(
            "There is no buzzer threads in selected subreddits. Try other subreddits!"
        )
    for telegram_message in telegram_message_list:
        update.message.reply_text(telegram_message)


def main() -> None:
    """Start the bot."""
    updater = Updater(TELEGRAM_API_KEY)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("NadaPraFazer", nada_pra_fazer))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
