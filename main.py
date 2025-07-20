from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hi {update.effective_user.first_name}, welcome to Laadobeast Bot! 😊")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started... use /start in Telegram")
app.run_polling()
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/about - Know about Laadobeast\n"
        "/uhrs - Clickworker UHRS link\n"
        "/earn - Daily earning ideas"
    )

app.add_handler(CommandHandler("help", help_command))
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 Laadobeast Bot created by Arnav to help you earn, learn & grow daily 💰📚")

app.add_handler(CommandHandler("about", about))
async def uhrs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 UHRS Access Link: https://prod.uhrs.playmsn.com")

app.add_handler(CommandHandler("uhrs", uhrs))
async def earn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Daily earning tips:\n"
        "1. Clickworker (UHRS unlock)\n"
        "2. Toloka\n"
        "3. YT automation\n"
        "4. Freelance jobs\n"
        "5. Telegram bots like this 😎"
    )

app.add_handler(CommandHandler("earn", earn))
