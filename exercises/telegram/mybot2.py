from telegram import Update
from telegram import ChatPermissions
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from telegram.ext import ApplicationBuilder
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler
from telegram.ext import filters,MessageHandler
from telegram.ext import ChatMemberHandler
from telegram.ext import CallbackContext    # I didn't find its method but it was in the DEFAUT_TYPE
from telegram.ext import CallbackQueryHandler

from dotenv import load_dotenv
from os import getenv
import logging 



#========================================================
# The main difference between send_message() 
# and reply_text() in the Telegram Bot API is
# how they handle the message context.
# send_message(): Sends a standalone message to the chat.
# reply_text():Sends a message that is visually linked to the original message in the chat.

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="This is the official RahemehrBot"
        )
    
#=======================================================

async def help(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """
    /start
/help
/echo
/welcome
/photo
/audio
/video
/delete
/leave
/ban
/unban
/mute
/unmute
/inline
    """
    )
  
#=======================================================
    
async def echo(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= update.message.text
        )

#=======================================================

async def welcome(update:Update, context:ContextTypes.DEFAULT_TYPE):
    new_member = update.message.new_chat_members
    print(new_member)
    for member in new_member:
        await update.message.reply_text("Welcome To The Rahemehr Group!")
    
#========================================================

async def photo(update:Update, context:ContextTypes.DEFAULT_TYPE):
    photo_url = "https://www.niksalehi.com/newspaper/wp-content/uploads/sites/44/2023/12/entegade-javad-khiabani.jpg"
    photo_caption= "این آبه ولی خاک ماست"
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo = photo_url,
        caption=photo_caption
        )

#========================================================
    
async def audio(update:Update, context:ContextTypes.DEFAULT_TYPE):
    audio_url = "https://sedatoseda.com/wp-content/uploads/Goal-in-goal-1.mp3"
    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio = audio_url
    )
    
#========================================================

async def send_audio(update:Update, context:ContextTypes.DEFAULT_TYPE):
    audio = update.message.audio
    await context.bot.send_audio(
        chat_id= update.effective_chat.id,
        audio = audio
    )
    
#========================================================

async def video(update:Update, context:ContextTypes.DEFAULT_TYPE):
    video_url = "https://ts19.tarafdari.com/contents/user516749/content-video/315892_0.mp4"
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video = video_url
    )

#========================================================

async def send_video(update:Update, context:ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    await context.bot.send_video(
    chat_id= update.effective_chat.id,
    video = video
    )

#========================================================
# for people who are in the black list

async def delete(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message = update.message
    await message.delete()
    
#========================================================
# delete the context that contains a sepecific word

async def delete(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message = update.message
    words_to_delete = ['فوش','خر','donkey']
    text = message.text.lower()
    if any(word in text for word in words_to_delete):
        await message.delete()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= f"Hey don\'t use this word {text}"
            )

#========================================================

async def leave_chat(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    await context.bot.leave_chat(chat_id)

#========================================================

async def ban_member(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_id = update.message.reply_to_message.from_user.id
    await context.bot.ban_chat_member(chat_id,user_id)

#========================================================

async def unban_member(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_id = update.message.reply_to_message.from_user.id
    await context.bot.unban_chat_member(chat_id,user_id)

#========================================================

async def mute(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_to_mute = update.message.reply_to_message.from_user.id
    chat_id = update.message.chat.id
    full_name = update.message.reply_to_message.from_user.full_name
    permissions = ChatPermissions(can_send_messages=False)
    await context.bot.restrict_chat_member(
        chat_id = chat_id,
        user_id = user_to_mute,
        permissions= permissions
    )
    await update.message.reply_text(
        f"{full_name} has been muted."
    )

#========================================================

async def unmute(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_to_unmute = update.message.reply_to_message.from_user.id
    chat_id = update.message.chat.id
    full_name = update.message.reply_to_message.from_user.full_name
    permissions = ChatPermissions(can_send_messages=True)
    await context.bot.restrict_chat_member(
        chat_id = chat_id,
        user_id = user_to_unmute,
        permissions= permissions
    )
    await update.message.reply_text(
        f"{full_name} has been unmuted."
    )
#========================================================

keyboard_main = [
    [
        InlineKeyboardButton("Backend", callback_data = 1),
        InlineKeyboardButton("Frontend", callback_data = 2)
    ],
    [
        InlineKeyboardButton("Full Stack Developer", callback_data = 3)
    ]
]
keyboard_back = [
    [
        InlineKeyboardButton("Back", callback_data= "back")
    ]
]
async def inline(update:Update, context:CallbackContext):
    reply_markup = InlineKeyboardMarkup(keyboard_main)
    await update.message.reply_text(
        "Please choose:",
        reply_markup = reply_markup
        )


async def button(update:Update, context:CallbackContext):
    query = update.callback_query
    await query.answer()
    option = query.data

    if option == "back":
        reply_markup = InlineKeyboardMarkup(keyboard_main)
        await query.edit_message_text(
            text= "Please choose:",
            reply_markup= reply_markup
        )
    else:
        reply_markup = InlineKeyboardMarkup(keyboard_back)
        await query.edit_message_text(
            text= f"selected option {option}: You need a lot of experience in each one",
            reply_markup= reply_markup
        )
#========================================================
    
if __name__ == "__main__":
        
    print("Bot is working")

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level= logging.INFO
    )

    load_dotenv()
    TOKEN = getenv('BOT_TOKEN')
    app = ApplicationBuilder().token(TOKEN).build()
    
    
    
    start_handler = CommandHandler('start',start)
    app.add_handler(start_handler)

    help_handler = CommandHandler('help',help)
    app.add_handler(help_handler)
    
    # echo_handler = MessageHandler(
    #     filters.TEXT & ~filters.COMMAND,
    #     echo
    #     )
    # app.add_handler(echo_handler)
    
    welcome_handler = MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome
        )
    app.add_handler(welcome_handler)
    
    photo_handler = CommandHandler("photo", photo)
    app.add_handler(photo_handler)
    
    audio_handler = CommandHandler("audio",audio)
    app.add_handler(audio_handler)  
    
    send_audio_handler = MessageHandler(filters.AUDIO, send_audio)
    app.add_handler(send_audio_handler)
      
    video_handler = CommandHandler("video",video)
    app.add_handler(video_handler)
    
    send_video_handler = MessageHandler(filters.VIDEO, send_video)
    app.add_handler(send_video_handler)
    
    # delete_handler = MessageHandler(filters.ALL, delete)
    # app.add_handler(delete_handler)
    
    # delete_handler = MessageHandler(
    #     filters.TEXT & ~filters.COMMAND,
    #     delete
    #     )
    # app.add_handler(delete_handler)
    
    app.add_handler(CommandHandler('leave', leave_chat))
    
    app.add_handler(CommandHandler('ban', ban_member))
    
    app.add_handler(CommandHandler('unban', unban_member))

    app.add_handler(CommandHandler("mute",mute))
    
    app.add_handler(CommandHandler("unmute",unmute))

    inline_handler = CommandHandler("inline", inline)
    app.add_handler(inline_handler)

    button_handler = CallbackQueryHandler(button)
    app.add_handler(button_handler)

    app.run_polling()
