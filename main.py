import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# Your bot token from BotFather
BOT_TOKEN = '7689660542:AAGzyhpRqkCKmV7eJVnvy-IjPBlxKKkmf3E'
KoyebServerURL = 'https://professional-janeta-sfshhsc-1d414042.koyeb.app/'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Handler for '/start' command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! Send me a link from a channel where I am admin.')

# Handler for incoming message links
async def handle_message(update: Update, context: CallbackContext) -> None:
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
            await update.message.reply_text(f"Download link for your content: {download_url}")

            # Save the file ID and generate a fake download link (This is a placeholder logic)
            save_to_server(message_id)

        except Exception as e:
            await update.message.reply_text("Error processing the message. Please ensure it's a valid message link.")
            logger.error(f"Error: {e}")
    else:
        await update.message.reply_text("Please send a valid Telegram message link.")

# Save file ID and generate the download link on Koyeb server
def save_to_server(message_id):
    # This is a placeholder function. You'd need to implement the actual file saving logic
    # and store the file (video, image, or document) on your server.
    
    # In this example, we just log the message ID and pretend to upload it
    logger.info(f"Saving content with message_id: {message_id} on the Koyeb server.")

    # Simulate file upload and creation of download link (you'd replace this logic with actual server code)
    return True

# Main function to set up the bot
def main():
    # Create the Application instance instead of Updater
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
