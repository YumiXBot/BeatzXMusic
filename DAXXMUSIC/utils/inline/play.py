import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from DAXXMUSIC import app
from DAXXMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "✄·─·─·─·─·─·─·─·─·─"
    elif 10 < umm < 20:
        bar = "-ˋˏ✄·─·─·─·─·─·─·─·─"
    elif 20 <= umm < 30:
        bar = "-ˋˏ-ˋˏ✄·─·─·─·─·─·─·─"
    elif 30 <= umm < 40:
        bar = "-ˋˏ-ˋˏ-ˋˏ✄·─·─·─·─·─·─"
    elif 40 <= umm < 50:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─·─·─·─"
    elif 50 <= umm < 60:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─·─·─"
    elif 60 <= umm < 70:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─·─"
    elif 70 <= umm < 80:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─"
    elif 80 <= umm < 95:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─"
    else:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·"
        
# Wynk ba-----------------------------------------------------------
    if 0 < umm <= 2:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 2 <= umm < 3:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 3 <= umm < 4:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 4 <= umm < 5:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 5 <= umm < 6:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 6 <= umm < 7:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 7 <= umm < 8:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 8 <= umm < 9:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 9 <= umm < 10:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 10 <= umm < 11:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 11 <= umm < 12:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 12 <= umm < 13:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢"
    elif 13 <= umm < 14:
        ba = "𝐀ℓσиє 𝐌υѕι¢"
    elif 14 <= umm < 15:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 15 <= umm < 16:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 16 <= umm < 17:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 17 <= umm < 18:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 18 <= umm < 19:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 19 <= umm < 20:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 20 <= umm < 21:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 21 <= umm < 22:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 22 <= umm < 23:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 23 <= umm < 24:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= umm < 25:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 25 <= umm < 26:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 26 <= umm < 27:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 27 <= umm < 28:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 28 <= umm < 29:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 29 <= umm < 30:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 30 <= umm < 31:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 31 <= umm < 32:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 32 <= umm < 33:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 33 <= umm < 34:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 34 <= umm < 35:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 35 <= umm < 36:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 36 <= umm < 37:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 37 <= umm < 38:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 38 <= umm < 39:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 39 <= umm < 40:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 40 <= umm < 41:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 41 <= umm < 42:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 42 <= umm < 43:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 43 <= umm < 44:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 44 <= umm < 45:
        ba = "𝐀ℓσиє 𝐌υѕι¢"
    elif 45 <= umm < 46:
        ba = "𝐀ℓσиє 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 46 <= umm < 47:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 47 <= umm < 48:
        ba = "𝐀ℓσиє 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 48 <= umm < 49:
        ba = "𝐀ℓσиє 𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    elif 49 <= umm < 50:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= umm < 51:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 51 <= umm < 52:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 52 <= umm < 53:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 53 <= umm < 54:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 54 <= umm < 55:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 55 <= umm < 56:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 56<= umm < 57:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 57 <= umm < 58:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 58 <= umm < 59:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 59 <= umm < 60:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= umm < 61:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢"
    elif 61 <= umm < 62:
        ba = "𝐀ℓσиє 𝐌υѕι¢"
    elif 62 <= umm < 63:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 63 <= umm < 64:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 64 <= umm < 65:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 65 <= umm < 66:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 66 <= umm < 67:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 67 <= umm < 68:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 68 <= umm < 69:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 69 <= umm < 70:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 70 <= umm < 71:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 71 <= umm < 72:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 72 <= umm < 73:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 73 <= umm < 74:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 74 <= umm < 75:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 75 <= umm < 76:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 76 <= umm < 77:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 77 <= umm < 78:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 78 <= umm < 79:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 79 <= umm < 80:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 80 <= umm < 81:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 81 <= umm < 82:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 82 <= umm < 83:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 83 <= umm < 84:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 84 <= umm < 85:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 85 <= umm < 86:
        ba = "𝐀ℓσиє 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 86 <= umm < 87:
        ba = "𝐀ℓσиє 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 87 <= umm < 88:
        ba = "𝐀ℓσиє 𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 88 <= umm < 89:
        ba = "𝐀ℓσиє 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 89 <= umm < 90:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 90 <= umm < 91:
        ba = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 91 <= umm < 92:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 92 <= umm < 93:
        ba = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 93 <= umm < 94:
        ba = "𝐀ℓσиє 𝐌υѕι¢"
    elif 94 <= umm < 95:
        ba = "𝐀ℓσиє 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 95 <= umm < 96:
        ba = "𝐀ℓσиє 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 96 <= umm < 97:
        ba = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐀ℓσиє 𝐌υ𝗌𝗂𝖼"
    elif 97 <= umm < 98:
        ba = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= umm < 99:
        ba = "𝐀ℓσиє 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        ba = "𝐀ℓσиє 𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
        
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(
                text=f"{ba}",
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(

                text="❀⋟ 𝐔ρ∂αтєѕ ⋞❀",

                url=f"{SUPPORT_CHAT}",

            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
