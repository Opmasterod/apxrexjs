import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Your bot token from BotFather
BOT_TOKEN = '7689660542:AAGzyhpRqkCKmV7eJVnvy-IjPBlxKKkmf3E'
KoyebServerURL = 'https://professional-janeta-sfshhsc-1d414042.koyeb.app/'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Handler for '/start' command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a link from a channel where I am admin.')

# Handler for incoming message links
def handle_message(update: Update, context: CallbackContext) -> None:
    # Extract the link from the message
    message_text = update.message.text
    if 'https://t.me/c/' in message_text:
        try:
            # Extract the channel ID and message ID from the link
            parts = message_text.split('/')
            channel_id = parts[3]
            message_id = parts[4]

            # Create the download link for your server
            download_url = f'{KoyebServerURL}{message_id}'

            # Respond with the download link
            update.message.reply_text(f"Download link for your content: {download_url}")

            # Save the file ID and generate a fake download link (This is a placeholder logic)
            save_to_server(message_id)

        except Exception as e:
            update.message.reply_text("Error processing the message. Please ensure it's a valid message link.")
            logger.error(f"Error: {e}")
    else:
        update.message.reply_text("Please send a valid Telegram message link.")

# Save file ID and generate the download link on Koyeb server
def save_to_server(message_id):
    # This is a placeholder function. You'd need to implement the actual file saving logic
    # and store the file (video, image, or document) on your server.
    # Example: Download the file from Telegram using the file_id and upload it to your server.
    
    # In this example, we just log the message ID and pretend to upload it
    logger.info(f"Saving content with message_id: {message_id} on the Koyeb server.")

    # Simulate file upload and creation of download link (you'd replace this logic with actual server code)
    return True

# Main function to set up the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
