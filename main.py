import requests
from telegram import InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Your bot token from BotFather
BOT_TOKEN = '7689660542:AAGzyhpRqkCKmV7eJVnvy-IjPBlxKKkmf3E'
KoyebServerURL = 'https://professional-janeta-sfshhsc-1d414042.koyeb.app/'

# Handler for incoming message links
async def handle_message(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text
    if 'https://t.me/c/' in message_text:
        try:
            parts = message_text.split('/')
            channel_id = parts[3]
            message_id = parts[4]

            # Fetch the media from Telegram API
            media_url = await get_media_url(channel_id, message_id, context)
            
            # Simulate file upload to Koyeb server (replace this with actual upload code)
            if media_url:
                file_response = upload_to_server(media_url, message_id)
                if file_response:
                    download_url = f'{KoyebServerURL}{message_id}'
                    await update.message.reply_text(f"Download link for your content: {download_url}")
                else:
                    await update.message.reply_text("Failed to upload content to the server.")
            else:
                await update.message.reply_text("Failed to fetch media from Telegram.")
        except Exception as e:
            await update.message.reply_text(f"Error processing the message. {e}")

# Function to get media URL from the Telegram API
async def get_media_url(channel_id, message_id, context):
    try:
        # Fetch the message details (including media)
        message = await context.bot.get_chat(channel_id).get_message(message_id)
        
        # Check the message type and get the appropriate media URL
        if message.video:
            return message.video.file_id
        elif message.document:
            return message.document.file_id
        elif message.photo:
            return message.photo[-1].file_id  # Get the highest resolution photo
        else:
            return None
    except Exception as e:
        print(f"Error fetching media URL: {e}")
        return None

# Upload the file to your server
def upload_to_server(media_url, message_id):
    try:
        # Here you'd need to implement the actual file upload logic to your Koyeb server
        # For example, you might use a POST request to upload the file to your server
        response = requests.post(f'{KoyebServerURL}/upload', data={'file_id': message_id, 'media_url': media_url})
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to upload file. Server response: {response.text}")
            return False
    except Exception as e:
        print(f"Error uploading file to server: {e}")
        return False

# Main function to set up the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
