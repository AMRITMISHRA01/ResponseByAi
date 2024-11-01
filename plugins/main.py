from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import *
from database import *

@Client.on_message(filters.command("start") & filters.incoming)
async def start_command(client, message):
    userMention = message.from_user.mention()
    if FSUB and not await get_fsub(client, message):
        return

    welcome_message = (
        "**👋 Welcome to Response By Ai!**\n\n"
        "🤖 I'm your personal AI assistant, crafted with love by ⏤͟͟͞͞ 🇮🇳 𝐓ʜᴇ 𝐂ᴀᴘᴛᴀɪɴ.\n\n"
        "✨ **Here’s what I can do for you:**\n"
        "1. Answer your queries with lightning speed! ⚡\n"
        "2. Generate stunning images that spark your imagination! 🎨\n"
        "3. Engage in delightful conversations that brighten your day! 💬\n\n"
        "Just click the buttons below to get started on this exciting journey! 🚀"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌟 ʜᴇʟᴘ", callback_data="help"),
         InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data="about")],
        [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/C0DE_SEARCH"),
         InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/AsuraaSupports")]
    ])

    await client.send_photo(chat_id=message.chat.id, photo="https://envs.sh/p_g.jpg", caption=welcome_message, reply_markup=keyboard)

@Client.on_callback_query()
async def handle_button_click(client, callback_query):
    if callback_query.data == "help":
        help_message = "**🔍 Choose a category for assistance:**\nLet's navigate through the possibilities together! 🌐"
        help_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💬 Cʜᴀᴛ Wɪᴛʜ Aɪ", callback_data="chatwithai"),
             InlineKeyboardButton("🖼️ ɪᴍᴀɢᴇ", callback_data="image")],
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start")]
        ])
        await edit_message(client, callback_query, help_message, help_keyboard)

    elif callback_query.data == "start":
        welcome_message = (
            "**👋 Welcome to Response By Ai!**\n\n"
            "🤖 I'm your personal AI assistant, crafted with love by ⏤͟͟͞͞ 🇮🇳 𝐓ʜᴇ 𝐂ᴀᴘᴛᴀɪɴ.\n\n"
            "✨ **Here’s what I can do for you:**\n"
            "1. Answer your queries with lightning speed! ⚡\n"
            "2. Generate stunning images that spark your imagination! 🎨\n"
            "3. Engage in delightful conversations that brighten your day! 💬\n\n"
            "Just click the buttons below to get started on this exciting journey! 🚀"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🌟 ʜᴇʟᴘ", callback_data="help"),
             InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data="about")],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/C0DE_SEARCH"),
             InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/AsuraaSupports")]
        ])

        await edit_message(client, callback_query, welcome_message, keyboard)

    elif callback_query.data == "chatwithai":
        chat_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
             InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/AsuraaSupports")]
        ])
        chat_message = (
            "**💬 Let's Chat with AI!**\n\n"
            "✨ Ready to explore? Use the commands below to ask me anything under the sun! ☀️\n\n"
            "/gpt - **Ask me anything with GPT-4o!** 💡\n"
            "/gemini - **Dive deep into questions with Gemini-Pro!** 🌌\n"
            "/llama - **Experience creativity with Llama-3.1-405b!** 🦙\n"
            "/blackbox - **Curious about BlackBoxAI-Pro? Just ask!** 📦"
        )
        await edit_message(client, callback_query, chat_message, chat_keyboard)

    elif callback_query.data == "image":
        image_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
             InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/AsuraaSupports")]
        ])
        await edit_message(client, callback_query, "**🖼️ Image Generation Awaits!**\n\n🎨 Just type **/draw** followed by your description, and watch the magic happen! ✨", image_keyboard)

    elif callback_query.data == "about":
        about_message = (
            "**ℹ️ About This Bot**\n\n"
            "👤 **Owner:** ⏤͟͟͞͞🇮🇳𝐓ʜᴇ 𝐂ᴀᴘᴛᴀɪɴ's </>\n"
            "🤖 **Functionality:**\n"
            "- Fast and accurate answers to your questions! ⚡\n"
            "- Generate beautiful images based on your prompts! 🎨\n"
            "- Engage in chat to learn and explore more! 💬\n\n"
            "🌐 **Powered by:** [Code Search API](https://codesearch.pages.dev/)\n\n"
            "🚀 Join me in this adventure and let's explore the limitless possibilities together!"
        )
        about_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
             InlineKeyboardButton("🔗 ʀᴇᴘᴏ", url="https://github.com/itzAsuraa/ResponseByAi")]
        ])
        await edit_message(client, callback_query, about_message, about_keyboard)

async def edit_message(client, callback_query, caption, reply_markup):
    try:
        await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)
    except Exception as e:
        print("Error editing message caption:", e)

    await client.answer_callback_query(callback_query.id)