from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 ᴩᴀᴜsᴇ 🙄",
            description=f"ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url=https://telegra.ph/file/5737cbb170b71c116f75d.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 ʀᴇsᴜᴍᴇ 😋",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/c760203b3d42bdeeab425.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 sᴋɪᴩ 🙂",
            description=f"sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
            thumb_url="https://telegra.ph/file/5737cbb170b71c116f75d.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 ᴇɴᴅ 🥺",
            description="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://telegra.ph/file/5737cbb170b71c116f75d.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥱 ʟᴏᴏᴩ 🥱",
            description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url=https://graph.org/file/c760203b3d42bdeeab425.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
