from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Load token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hi {update.effective_user.first_name}, welcome to arnav Bot! 😊")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are some commands you can use:\n/start - Start the bot\n/help - Show this help\n/about - Info about me\n/love - Cute msg")

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Laadobeast bot made with ❤️ by Arnav. I’m here to help and spread joy!")

# /love command
async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("welcome to laadobeast love")

# Create the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add all command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("love", love))

print("Bot started... use /start in Telegram")
app.run_polling()

