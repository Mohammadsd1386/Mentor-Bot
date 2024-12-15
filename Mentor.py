import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters
import re

# Telegram bot token
TELEGRAM_TOKEN = '7674911293:AAEH1p69B_tH0PRSpjovRQ_PUb2yqrGW57k'
# OpenAI API key
OPENAI_API_KEY = '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'

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# The start command that is shown when the user starts the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your mentor bot. Ask me anything.')

# Function to handle incoming messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text  # User message

    # Check for mentions in the message
    mention_pattern = r'@(\w+)'  # Mention pattern
    mentions = re.findall(mention_pattern, user_message)

    if mentions:
        reply = "It looks like you tagged someone!"
    else:
        # Process the message with OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another OpenAI model
            prompt=user_message,
            max_tokens=150
        )
        reply = response.choices[0].text.strip()

    # Send the reply to the user
    await update.message.reply_text(reply)

# Main function to run the bot
def main() -> None:
    # Set up the bot with Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    application.run_polling()

if __name__ == '__main__':
    main()
